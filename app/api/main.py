from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.generation.generate_answers import (
    answer_incident,
    chat_client,
    embedding_client,
    qdrant,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    chat_client.close()
    embedding_client.close()
    qdrant.close()


app = FastAPI(
    title="IT Incident Copilot",
    description="RAG-powered incident investigation assistant",
    version="0.1.0",
    lifespan=lifespan,
)


class IncidentRequest(BaseModel):
    question: str = Field(min_length=5, max_length=5000)


class IncidentResponse(BaseModel):
    question: str
    answer: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/incident/analyze", response_model=IncidentResponse)
def analyze_incident(request: IncidentRequest):
    try:
        answer = answer_incident(request.question)

        return IncidentResponse(
            question=request.question,
            answer=answer,
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Incident analysis failed. Check server logs.",
        )