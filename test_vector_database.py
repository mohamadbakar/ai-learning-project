from embeddings import create_embedding
from vector_database import save_chunk, search_chunks


# Define sample document chunks
chunks = [
    {
        "id": "chunk_1",
        "text": "Python is a programming language used in AI development.",
        "page": 1
    },
    {
        "id": "chunk_2",
        "text": "Machine learning allows computers to learn from data.",
        "page": 2
    },
    {
        "id": "chunk_3",
        "text": "FastAPI is used to build web APIs with Python.",
        "page": 3
    }
]


# Generate embeddings and save the chunks
for chunk in chunks:

    embedding = create_embedding(chunk["text"])

    save_chunk(
        chunk_id=chunk["id"],
        text=chunk["text"],
        embedding=embedding,
        page_number=chunk["page"]
    )


# Search using a question with different wording
question = "How can Python be used to create AI applications?"

query_embedding = create_embedding(question)

results = search_chunks(query_embedding, number_of_results=3)


# Display the matching chunks
for result in results:

    print("\nMatching text:", result["text"])
    print("Page:", result["page_number"])
    print("Distance:", result["distance"])