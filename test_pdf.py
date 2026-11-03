from pdf_processor import process_pdf


# Process the sample PDF
chunks = process_pdf("sample.pdf")


# Print the total number of chunks
print(f"Total chunks: {len(chunks)}")


# Display each chunk with its page number
for index, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {index}")
    print(f"Page: {chunk['page_number']}")
    print(chunk["text"])