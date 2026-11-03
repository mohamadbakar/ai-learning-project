from embeddings import create_embedding
from vector_database import search_chunks
from llm import ask_ollama


# Answer a question using information from indexed documents
def answer_from_documents(question , filename=None):

    # Convert the question into an embedding
    query_embedding = create_embedding(question)

    # Retrieve the three most relevant chunks
    relevant_chunks = search_chunks(
        query_embedding,
        number_of_results=6,
        filename=filename
    )

    # Combine the retrieved text into one context
    context = "\n\n".join(
        [
            f"File: {chunk['filename']}\n"
        f"Page {chunk['page_number']}:\n"
        f"{chunk['text']}"
        for chunk in relevant_chunks
        ]
    )

    # Build a prompt using the retrieved document context
    prompt = f"""
    Answer the question using only the information in the context below.

    Include the filename and page number when citing information.
    Do not invent information.

    If the answer is not available, say:
    "I could not find the answer in the document."

    Context:
    {context}

    Question:
    {question}
    """

    # Generate an answer using the local LLM
    answer = ask_ollama(prompt)

    return {
        "answer": answer,
        "sources": relevant_chunks
    }