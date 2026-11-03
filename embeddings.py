import requests


# Convert text into an embedding vector using Ollama
def create_embedding(text):

    response = requests.post(
        "http://host.docker.internal:11434/api/embed",
        json={
            "model": "nomic-embed-text",
            "input": text
        },
        timeout=120
    )

    # Raise an error if the request failed
    response.raise_for_status()

    # Extract the embedding vector from the response
    embedding = response.json()["embeddings"][0]

    return embedding