from rag import answer_from_documents


# Ask a question about the indexed PDF
question = "Which areas of background are required for the candidate?"

# Generate an answer using RAG
result = answer_from_documents(question)


# Display the generated answer
print("\nAnswer:")
print(result["answer"])


# Display the source pages
print("\nSources:")

for source in result["sources"]:
    print(f"Page: {source['page_number']}")
    print(f"Text: {source['text'][:200]}")
    print("-" * 40)