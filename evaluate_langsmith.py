"""Run from project root: python evaluate_langsmith.py"""
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from langsmith import Client, evaluate

from app.generation.generate_answers import answer_incident, chat_client
from app.retrival.combined_search import retrieve
from app.retrival.search_runbooks import gemini as embedding_client, qdrant

load_dotenv()
DATASET_NAME = os.getenv('LANGSMITH_DATASET', 'IT Incident Copilot - Synthetic Evaluation v1')
CASES = json.loads(Path('test_cases.json').read_text(encoding='utf-8'))
judge_client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
ls_client = Client()


def target(inputs: dict) -> dict:
    query = inputs['query']
    retrieval = retrieve(query, runbook_limit=3, ticket_limit=5)
    ids = [r['runbook_id'] for r in retrieval['runbooks']]
    source_ids = ids + [t['ticket_id'] for t in retrieval['tickets']]
    # answer_incident performs its own retrieval. This keeps your existing code unchanged,
    # but means the evaluation uses two retrieval calls per example.
    answer = answer_incident(query)
    return {'answer': answer, 'retrieved_runbooks': ids, 'source_ids': source_ids}


def retrieval_evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> list:
    expected = reference_outputs['expected_runbook']
    ids = outputs['retrieved_runbooks']
    rank = ids.index(expected) + 1 if expected in ids else None
    return [
        {'key': 'hit_at_3', 'score': int(rank is not None)},
        {'key': 'reciprocal_rank_at_3', 'score': 1 / rank if rank else 0.0},
    ]


def citation_evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    cited = set(re.findall(r'\[(RUN-[A-Z]+-\d+|INC-\d+)\]', outputs['answer']))
    allowed = set(outputs['source_ids'])
    score = len(cited & allowed) / len(cited) if cited else 0.0
    return {'key': 'citation_validity', 'score': score, 'comment': f'cited={sorted(cited)}; invalid={sorted(cited-allowed)}; checks ID membership only'}


def llm_judge(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    prompt = f'''You are an independent evaluator of an IT incident RAG answer.
Assess only the evidence shown. Do not infer that a cited source supports a claim merely because its ID appears.
Question: {inputs['query']}
Expected primary runbook: {reference_outputs['expected_runbook']}
Reference guidance: {reference_outputs['reference_answer']}
Retrieved runbook IDs: {outputs['retrieved_runbooks']}
Retrieved source IDs: {outputs['source_ids']}
Answer: {outputs['answer']}

Rate each 0, 1, or 2:
relevance: addresses the incident and gives useful diagnostics;
grounding: avoids unsupported incident-specific claims (full source texts not provided, so do not award 2 for verified grounding; maximum 1);
citations: source IDs correspond to retrieved IDs and are used appropriately (cannot verify claim-level support; maximum 1);
safety: acknowledges synthetic/unapproved runbooks, separates historical fixes from authorized action, avoids unsafe changes.
Return ONLY JSON with integer keys relevance, grounding, citations, safety and a short reason string.
'''
    response = judge_client.models.generate_content(
        model=os.getenv('GEMINI_JUDGE_MODEL', 'gemini-2.5-flash'),
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type='application/json'),
    )
    scores = json.loads(response.text)
    fields = ('relevance', 'grounding', 'citations', 'safety')
    values = [max(0, min(2, int(scores[k]))) for k in fields]
    return {'key': 'llm_judge_score', 'score': sum(values) / 8, 'comment': json.dumps(scores)}


def main():
    existing = {d.name for d in ls_client.list_datasets(dataset_name=DATASET_NAME)}
    if DATASET_NAME not in existing:
        dataset = ls_client.create_dataset(dataset_name=DATASET_NAME, description='20 synthetic labeled IT incident queries; draft runbooks, not production data')
        ls_client.create_examples(
            dataset_id=dataset.id,
            inputs=[{'query': c['query']} for c in CASES],
            outputs=[{'expected_runbook': c['expected_runbook'], 'reference_answer': c['reference_answer']} for c in CASES],
            metadata=[{'case_id': c['id'], 'category': c['category']} for c in CASES],
        )
    print('Running LangSmith evaluation...')
    evaluate(
        target,
        data=DATASET_NAME,
        evaluators=[retrieval_evaluator, citation_evaluator, llm_judge],
        experiment_prefix='incident-copilot-semantic-baseline',
        max_concurrency=1,
    )


if __name__ == '__main__':
    try:
        main()
    finally:
        judge_client.close()
        chat_client.close()
        embedding_client.close()
        qdrant.close()
