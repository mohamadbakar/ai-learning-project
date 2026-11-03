

import chromadb


# Store ChromaDB data in a persistent volume
client = chromadb.PersistentClient(path="/app/chroma_db")

# Create or open the document collection
collection = client.get_or_create_collection(
    name="documents"
)


# Store or update a text chunk and its metadata
def save_chunk(chunk_id, text, embedding, page_number, filename):

    collection.upsert(
        ids=[chunk_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "page_number": page_number,
                "filename": filename
            }
        ]
    )

# Search for document chunks with similar meaning
def search_chunks(query_embedding, number_of_results=3 , filename=None):

     # Build search filters when a filename is provided
    filters = {"filename": filename} if filename else None

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=number_of_results,
        where=filters
    )
    # Format the search results
    matches = []

    for index in range(len(results["ids"][0])):

        matches.append({
            "text": results["documents"][0][index],
            "page_number": results["metadatas"][0][index]["page_number"],
            "filename": results["metadatas"][0][index]["filename"],
            "distance": results["distances"][0][index]
        })

    return matches