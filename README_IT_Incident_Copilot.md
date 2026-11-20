# 🛡️ IT Incident Copilot

**RAG-powered IT incident investigation assistant** built with Google Gemini, Qdrant, FastAPI, Streamlit, and Docker.

IT Incident Copilot helps support engineers investigate reported problems by retrieving troubleshooting runbooks, comparing similar historical incidents, and generating structured responses with source IDs, diagnostic checks, verification, and escalation guidance.

## Features

- **Two-source semantic retrieval:** Searches runbooks and resolved incident tickets in separate Qdrant collections.
- **Parent–child retrieval:** Indexes compact runbook sections, deduplicates matches, and expands them into full runbooks for generation.
- **Grounded incident analysis:** Gemini generates structured answers referencing runbook and ticket IDs.
- **Web interface and API:** Streamlit frontend and FastAPI `POST /incident/analyze` endpoint.

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| LLM | Google Gemini |
| Embeddings | `gemini-embedding-001` (768 dimensions) |
| Vector database | Qdrant (cosine similarity) |
| API | FastAPI |
| UI | Streamlit |
| Containerization | Docker |
| Evaluation | LangSmith |

## Architecture

```text
User → Streamlit → FastAPI → Query embedding (Gemini)
                                ↓
                         Qdrant retrieval
                         ↙             ↘
                   Runbook chunks    Ticket records
                         ↘             ↙
                   Parent expansion + evidence
                                ↓
                      Gemini answer generation
                                ↓
                 Analysis, diagnostics, citations
```

## Knowledge Base

The demonstration corpus is **synthetic**: 22 draft runbooks (66 child chunks) and 1,000 resolved-incident examples (1,000 ticket vectors), for **1,066 indexed vectors**. Runbooks are **not approved operational procedures**; historical fixes are supporting evidence, not guaranteed remedies.

## Example Incident

**Input:** “Several employees cannot access internal applications because DNS hostnames are failing to resolve.”

**Typical output:** Incident summary, possible DNS-related causes, authorized read-only diagnostic checks, verification criteria, and escalation guidance, citing the DNS runbook (`RUN-NET-007`) and relevant historical ticket IDs. The answer explicitly flags the evidence as synthetic and draft.

## Evaluation Results

The RAG pipeline was evaluated with **LangSmith** using 20 labeled synthetic IT incident scenarios.

| Evaluation Metric | Result |
|---|---|
| Test cases | 20 |
| Successful executions | 20/20 (100%) |
| Hit@3 | **100%** |
| MRR@3 | **1.00** |
| Citation validity | **100%** |
| LLM-as-a-judge score | **0.75 / 1.00** |
| Average end-to-end latency | **29.65 seconds** |

**Findings:** The expected runbook ranked first for all 20 queries, and all extracted citation IDs were present in the retrieved source IDs. All runs completed successfully.

**Evaluation caveats:** This is a small synthetic benchmark, not a production accuracy claim. Citation validity measures ID membership, not claim-level support. The judge did not receive full source texts, so grounding and citation subscores were capped; **0.75 is a rubric score, not 75% factual accuracy**.

## Running Locally

**Prerequisites:** Python, Docker Desktop, and a Gemini API key.

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create `.env` in the project root:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

3. Start Qdrant using Docker (if your Compose file contains only Qdrant, or start only that service):

   ```bash
   docker compose up -d qdrant
   ```

4. From the project root, start FastAPI in **Terminal 1**:

   ```bash
   python -m uvicorn app.api.main:app --reload
   ```

5. Start Streamlit in **Terminal 2**:

   ```bash
   python -m streamlit run app/frontend/streamlit_app.py
   ```

Open **http://localhost:8501** for the UI or **http://localhost:8000/docs** for the API. Qdrant must already contain the indexed runbooks and tickets.

**Alternative full-container setup:** If your Compose file defines the API and Streamlit services as well, use `docker compose up -d --build` and do not start them again manually. Initialize the vector database first if it is empty.

## Limitations and Future Work

- Synthetic data does not establish performance on real production incidents.
- Runbooks require environment-owner approval before operational use.
- Dense vector search only; hybrid keyword search and reranking are future improvements.
- Generated citations and confidence statements require stronger automated validation.
- Gemini API access and quota are required; the application is not fully offline.

**Status:** Functional individual-project prototype for educational and demonstration use. Operational changes require appropriate authorization and human review.
