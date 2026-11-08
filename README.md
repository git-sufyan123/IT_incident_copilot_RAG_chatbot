# 🛡️ IT Incident Copilot

**RAG-powered IT incident investigation assistant** built with Google Gemini, Qdrant, FastAPI, Streamlit, and Docker.

IT Incident Copilot helps support engineers investigate reported problems by finding relevant troubleshooting runbooks, comparing similar historical incidents, and producing a structured response with source IDs, diagnostic checks, verification, and escalation guidance.

## Features

- **Two-source semantic retrieval:** Searches troubleshooting runbooks and resolved incident tickets in separate Qdrant collections.
- **Parent–child retrieval:** Indexes compact runbook sections, deduplicates matches, and expands them into full runbooks before generation.
- **Grounded incident analysis:** Gemini produces structured answers referencing runbook and ticket IDs.
- **Web interface and API:** Streamlit chat frontend and FastAPI `POST /incident/analyze` endpoint.


## Technology stack

| Layer | Technology |
|---|---|
| Language | Python |
| LLM | Google Gemini |
| Embeddings | `gemini-embedding-001` (768 dimensions) |
| Vector database | Qdrant (cosine similarity) |
| API | FastAPI |
| UI | Streamlit |

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

## Knowledge base

The demonstration corpus is **synthetic**: 22 draft runbooks (66 child chunks) and 1,000 resolved-incident examples (1,000 ticket vectors), for **1,066 indexed vectors**. Runbooks are **not approved operational procedures**; historical fixes are supporting evidence, not guaranteed remedies.


## Example incident

**Input:** “Several employees cannot access internal applications because DNS hostnames are failing to resolve.”

**Typical output:** Incident summary, possible DNS-related causes, authorized read-only diagnostic checks, verification criteria, and escalation guidance, citing the matching DNS runbook (`RUN-NET-007`) and relevant historical ticket IDs. The answer explicitly flags the evidence as synthetic and draft.
```

## Limitations and future work

- Synthetic data does not establish performance on real production incidents.
- Runbooks require environment-owner approval before operational use.
- Dense vector search only; hybrid keyword search and reranking are future improvements.
- Generated citations and confidence statements require stronger automated validation.
- Gemini API access and quota are required; the application is not fully offline.

**Status:** Functional individual-project prototype for educational and demonstration use. Operational changes require appropriate authorization and human review.
