import os
import numpy as np

from dotenv import load_dotenv
from google import genai
from google.genai import types
from qdrant_client import QdrantClient

load_dotenv()

COLLECTION = "it_incident_runbooks"

gemini = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333")
)


def embed_query(query: str) -> list[float]:
    response = gemini.models.embed_content(
        model=os.getenv(
            "GEMINI_EMBEDDING_MODEL",
            "gemini-embedding-001"
        ),
        contents=query,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=768
        )
    )

    vector = np.asarray(
        response.embeddings[0].values,
        dtype=np.float32
    )

    return (vector / np.linalg.norm(vector)).tolist()


def search_runbooks(query: str, limit: int = 5):
    query_vector = embed_query(query)

    response = qdrant.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=limit,
        with_payload=True
    )

    return response.points


if __name__ == "__main__":
    try:
        while True:
            query = input("\nDescribe an IT incident (or 'exit'): ").strip()

            if query.lower() == "exit":
                break

            if not query:
                continue

            results = search_runbooks(query)

            for rank, point in enumerate(results, start=1):
                payload = point.payload

                print(f"\n--- Result {rank} ---")
                print("Score:", round(point.score, 4))
                print("Runbook:", payload["parent_id"])
                print("Section:", payload["section"])
                print("Status:", payload["status"])
                print("Text preview:", payload["text"][:300])
    finally:
        gemini.close()
        qdrant.close()