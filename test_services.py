import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from qdrant_client import QdrantClient

load_dotenv()

def test_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    chat_model = os.getenv("GEMINI_CHAT_MODEL")
    embedding_model = os.getenv("GEMINI_EMBEDDING_MODEL")

    if not api_key or api_key == "replace_me":
        raise ValueError("GEMINI_API_KEY is missing from .env")

    client = genai.Client(api_key=api_key)

    # Test chat generation
    response = client.models.generate_content(
        model=chat_model,
        contents="Reply with exactly: Gemini connection successful"
    )

    print("\n--- GEMINI CHAT ---")
    print(response.text)

    # Test document embedding
    embedding_response = client.models.embed_content(
        model=embedding_model,
        contents="A user cannot connect to the corporate VPN.",
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=768
        )
    )

    vector = embedding_response.embeddings[0].values

    print("\n--- GEMINI EMBEDDING ---")
    print("Vector dimensions:", len(vector))
    print("First 5 values:", vector[:5])

    assert len(vector) == 768, "Unexpected embedding dimension"

    client.close()


def test_qdrant():
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    client = QdrantClient(url=qdrant_url)

    collections = client.get_collections()

    print("\n--- QDRANT ---")
    print("Connection successful!")
    print("Existing collections:", [
        collection.name for collection in collections.collections
    ])

    client.close()


if __name__ == "__main__":
    test_gemini()
    test_qdrant()
    print("\nAll connection tests passed!")