from pypdf import PdfReader


# Extract text from a PDF file
def extract_text_from_pdf(pdf_path):

    # Open the PDF file
    reader = PdfReader(pdf_path)

    # Store the extracted text from each page
    pages = []

    # Loop through all PDF pages
    for page_number, page in enumerate(reader.pages, start=1):

        # Extract text from the current page
        text = page.extract_text() or ""

        # Store the page number and its text
        pages.append({
            "page_number": page_number,
            "text": text
        })

    # Return all extracted pages
    return pages

# Split text into smaller chunks
def split_text_into_chunks(text, chunk_size=500, overlap=50):

    # Store the generated chunks
    chunks = []

    # Start from the beginning of the text
    start = 0

    # Continue until we reach the end of the text
    while start < len(text):

        # Calculate the end position of the current chunk
        end = start + chunk_size

        # Extract the current chunk
        chunk = text[start:end]

        # Add the chunk to the list
        chunks.append(chunk)

        # Move forward while keeping some overlapping text
        start += chunk_size - overlap

    # Return all generated chunks
    return chunks

# Extract and split text while preserving page numbers
def process_pdf(pdf_path):

    # Extract all pages from the PDF
    pages = extract_text_from_pdf(pdf_path)

    # Store all generated chunks
    all_chunks = []

    # Process each page separately
    for page in pages:

        # Split the current page into chunks
        chunks = split_text_into_chunks(page["text"])

        # Store each chunk with its page number
        for chunk in chunks:

            if chunk.strip():

                all_chunks.append({
                    "page_number": page["page_number"],
                    "text": chunk
                })

    return all_chunks