# Import BaseModel to define and validate the structure of incoming data
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import (
    create_database,
    save_conversation,
    get_conversations
)
import requests
from llm import ask_ollama
from rag import answer_from_documents
from fastapi import UploadFile, File
from pathlib import Path
from document_indexer import index_pdf


app = FastAPI()

# Define the request data for document questions
class QuestionRequest(BaseModel):
    question: str
    filename: str | None = None

# Create the database when the application starts
@app.on_event("startup")
def startup():
    create_database()

#1--------------------------------------------------------------------

@app.post("/ask")

def answer_question(data: QuestionRequest):

    question = data.question
    # Check if the question is empty or contains only spaces
    if not question.strip():

        # Return an HTTP 400 error if the question is invalid
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )


    
       # Generate the answer using Ollama
    try:
        answer = ask_ollama(question)

    # Handle Ollama errors
    except RuntimeError as error:
       raise HTTPException(
        status_code=502,
        detail=str(error)
      )

    # Save the question and answer in the database
    save_conversation(question, answer)

    return {
        "question": question,
        "answer": answer
    }

#2--------------------------------------------------------------------


# GET endpoint: Retrieve all saved conversations
@app.get("/conversations")
def read_conversations():

    conversations = get_conversations()

    return [
        {
            "id": conversation[0],
            "question": conversation[1],
            "answer": conversation[2]
        }
        for conversation in conversations
    ]

#3--------------------------------------------------------------------


# Answer questions using indexed PDF documents
@app.post("/ask-document")
def ask_document(data: QuestionRequest):

    question = data.question

    # Reject empty questions
    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    # Generate an answer using RAG
    try:
        result = answer_from_documents(question, filename=data.filename)

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to Ollama"
        )

    # Save the conversation in the database
    save_conversation(question, result["answer"])

    # Return the answer and its sources
    return {
        "question": question,
        "filename": data.filename,
        "answer": result["answer"],
        "sources": result["sources"]
    }

#4--------------------------------------------------------------------

# Define the folder used to store uploaded PDFs
UPLOAD_DIR = Path("uploads")

# Create the upload folder if it does not exist
UPLOAD_DIR.mkdir(exist_ok=True)


# Upload and index a PDF document
@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    # Check that the uploaded file is a PDF
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Create the file path
    file_path = UPLOAD_DIR / Path(file.filename).name

    # Save the uploaded file
    with file_path.open("wb") as uploaded_file:
        uploaded_file.write(file.file.read())

    # Index the PDF document
    number_of_chunks = index_pdf(str(file_path))

    return {
        "filename": file.filename,
        "chunks_indexed": number_of_chunks,
        "message": "PDF uploaded and indexed successfully"
    }