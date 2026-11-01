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


app = FastAPI()

# The request must contain a field called "question" with a string value
class QuestionRequest(BaseModel):
    question: str

# Create the database when the application starts
@app.on_event("startup")
def startup():
    create_database()


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

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to Ollama"
        )

    # Save the question and answer in the database
    save_conversation(question, answer)

    return {
        "question": question,
        "answer": answer
    }



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