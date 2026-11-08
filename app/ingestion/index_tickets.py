import pandas as pd
import uuid

from qdrant_client import models

from chunks_tickets import chunk_ticket
from index_runbooks import (
    qdrant,
    embed_chunks,
    DIM,
)


COLLECTION = "it_incident_tickets"


def main():
    df = pd.read_csv("data/resolved_it_incidents_1000.csv")
    chunks = [chunk_ticket(row) for row in df.to_dict("records")]

    if not qdrant.collection_exists(COLLECTION):
        qdrant.create_collection(
            collection_name=COLLECTION,
            vectors_config=models.VectorParams(
                size=DIM,
                distance=models.Distance.COSINE,
            ),
        )

    batch_size = 8

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start:start + batch_size]
        vectors = embed_chunks([chunk["text"] for chunk in batch])

        points = [
            models.PointStruct(
                id=str(uuid.uuid5(uuid.NAMESPACE_URL, chunk["chunk_id"])),
                vector=vector,
                payload=chunk,
            )
            for chunk, vector in zip(batch, vectors)
        ]

        qdrant.upsert(
            collection_name=COLLECTION,
            points=points,
            wait=True,
        )

        print(f"Indexed {min(start + batch_size, len(chunks))}/{len(chunks)}")

    print(
        "Total ticket points:",
        qdrant.count(collection_name=COLLECTION, exact=True).count,
    )


if __name__ == "__main__":
    try:
        main()
    finally:
        from index_runbooks import gemini
        gemini.close()
        qdrant.close()
