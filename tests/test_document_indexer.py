from document_indexer import index_pdf


# Index the sample PDF document
number_of_chunks = index_pdf("sample.pdf")


# Display the indexing result
print(f"Successfully indexed {number_of_chunks} chunks.")