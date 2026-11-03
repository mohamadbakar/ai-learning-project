# AI Document Assistant

A local AI-powered application that allows users to upload PDF documents and ask questions about their content.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate answers with source references and page numbers.

## Features

- Upload and process PDF documents.
- Extract text and split it into smaller chunks.
- Generate text embeddings using Ollama.
- Store and search document embeddings using ChromaDB.
- Ask questions about uploaded documents.
- Generate answers using a local Llama model.
- Include source references and page numbers in answers.
- Store conversation history using SQLite.
- Expose functionality through a REST API built with FastAPI.
- Run the application using Docker and Docker Compose.
- Persist uploaded documents and vector database data using Docker volumes.

## Tech Stack

- **Python** – Main programming language
- **FastAPI** – REST API framework
- **Ollama** – Local LLM and embedding model runtime
- **Llama 3.2** – Language model
- **Nomic Embed Text** – Embedding model
- **ChromaDB** – Vector database
- **SQLite** – Conversation storage
- **PyPDF** – PDF text extraction
- **Docker** – Application containerization
- **Docker Compose** – Application and volume management
- **Pytest** – Automated testing

## How It Works

1. The user uploads a PDF document.
2. The application extracts text from the PDF.
3. The extracted text is divided into smaller chunks.
4. Each chunk is converted into an embedding vector.
5. The embeddings and document metadata are stored in ChromaDB.
6. When the user asks a question, the question is converted into an embedding.
7. ChromaDB retrieves the most relevant document chunks.
8. The retrieved information is sent to the Llama model.
9. The model generates an answer based on the retrieved context, including source references.

## Project Structure

```text
ai-learning-project/
│
├── tests/
│   ├── test_main.py
│   ├── test_pdf.py
│   ├── test_embeddings.py
│   ├── test_vector_database.py
│   ├── test_document_indexer.py
│   └── test_rag.py
│
├── uploads/
├── chroma_db/
│
├── main.py
├── database.py
├── llm.py
├── pdf_processor.py
├── embeddings.py
├── vector_database.py
├── document_indexer.py
├── rag.py
│
├── sample.pdf
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11+
- Docker Desktop
- Ollama

Required Ollama models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Run with Docker Compose

1. Start Docker Desktop.
2. Make sure Ollama is running on your computer.
3. From the project directory, run:

```bash
docker compose up -d --build
```

4. Open the API documentation:

http://localhost:8000/docs

## Stop the Application

```bash
docker compose down
```

Docker volumes are preserved when using this command.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/upload-pdf` | Upload and index a PDF |
| POST | `/ask-document` | Ask questions about documents |
| POST | `/ask` | Ask the language model |
| GET | `/conversations` | Retrieve conversation history |

## Testing

Run the automated tests with:

```bash
pytest
```

## Sample Document

The repository includes `sample.pdf`, which can be used to test PDF uploading and document question answering.

## Project Goal

This project was built to gain practical experience in developing AI-powered backend applications, understanding RAG pipelines, working with local language models, and deploying Python applications using Docker.