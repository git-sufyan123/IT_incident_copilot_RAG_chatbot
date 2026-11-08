import os
import uuid
import numpy as np

from dotenv import load_dotenv
from google import genai
from google.genai import types
from qdrant_client import QdrantClient, models

from load_runbooks import load_runbooks
from chunk_runbooks import chunk_runbook

load_dotenv()

DIM = 768
COLLECTION = "it_incident_runbooks"

gemini = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333"),timeout=120
)


def normalize(vector):
    vector = np.asarray(vector, dtype=np.float32)
    norm = np.linalg.norm(vector)

    if norm == 0:
        raise ValueError("Zero-length embedding")

    return (vector / norm).tolist()


def embed_chunks(texts):
    response = gemini.models.embed_content(
        model=os.getenv(
            "GEMINI_EMBEDDING_MODEL",
            "gemini-embedding-001"
        ),
        contents=texts,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=DIM
        )
    )

    return [
        normalize(item.values)
        for item in response.embeddings
    ]


def main():
    runbooks = load_runbooks("data/runbooks.jsonl")

    chunks = []
    for runbook in runbooks:
        chunks.extend(chunk_runbook(runbook))

    if not qdrant.collection_exists(COLLECTION):
        qdrant.create_collection(
            collection_name=COLLECTION,
            vectors_config=models.VectorParams(
                size=DIM,
                distance=models.Distance.COSINE
            )
        )

    batch_size = 16

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start:start + batch_size]

        vectors = embed_chunks(
            [chunk["text"] for chunk in batch]
        )

        if len(vectors) != len(batch):
            raise ValueError("Embedding count mismatch")

        points = []

        for chunk, vector in zip(batch, vectors):
            point_id = str(uuid.uuid5(
                uuid.NAMESPACE_URL,
                chunk["chunk_id"]
            ))

            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=vector,
                    payload=chunk
                )
            )

        qdrant.upsert(
            collection_name=COLLECTION,
            points=points,
            wait=True
        )

        print(
            f"Indexed {min(start + batch_size, len(chunks))}"
            f"/{len(chunks)} chunks"
        )

    print("Total indexed points:",
          qdrant.count(
              collection_name=COLLECTION,
              exact=True
          ).count)


if __name__ == "__main__":
    try:
        main()
    finally:
        gemini.close()
        qdrant.close()
