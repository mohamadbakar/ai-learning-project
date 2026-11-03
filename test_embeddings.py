from embeddings import create_embedding


# Convert a sample sentence into an embedding vector
text = "Artificial Intelligence helps computers understand information."

embedding = create_embedding(text)


# Print the vector size
print("Embedding dimensions:", len(embedding))


# Print only the first five numbers
print("First five values:", embedding[:5])