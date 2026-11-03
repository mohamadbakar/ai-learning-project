from pdf_processor import process_pdf
from embeddings import create_embedding
from vector_database import save_chunk
from pathlib import Path


# Process and index a complete PDF document
def index_pdf(pdf_path):

    # Extract the PDF filename
    filename = Path(pdf_path).name

    # Extract and split the PDF into chunks
    chunks = process_pdf(pdf_path)

    # Process each chunk and save it in ChromaDB
    for index, chunk in enumerate(chunks):

        # Generate an embedding for the chunk
        embedding = create_embedding(chunk["text"])

        # Create a unique ID for the chunk
        chunk_id = f"{filename}_chunk_{index}"

        # Save the chunk and its metadata
        save_chunk(
            chunk_id=chunk_id,
            text=chunk["text"],
            embedding=embedding,
            page_number=chunk["page_number"],
            filename=filename
        )

    # Return the number of indexed chunks
    return len(chunks)