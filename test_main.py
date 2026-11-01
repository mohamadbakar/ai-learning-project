# Import FastAPI's test client
from fastapi.testclient import TestClient

# Import patch to replace real functions with mock functions
from unittest.mock import patch

# Import our FastAPI application
from main import app


# Create a test client to send requests to our API
client = TestClient(app)


# Test that the API rejects an empty question
def test_empty_question():

    # Send a POST request with an empty question
    response = client.post(
        "/ask",
        json={"question": ""}
    )

    # Check that the API returns status code 400
    assert response.status_code == 400


# Replace the real Ollama function with a mock function
@patch("main.ask_ollama")

# Replace the real database save function with a mock function
@patch("main.save_conversation")

# Test that the API handles a valid question
def test_valid_question(mock_save, mock_ollama):

    # Define the fake answer returned by the mock AI
    mock_ollama.return_value = "AI is Artificial Intelligence."

    # Send a POST request with a valid question
    response = client.post(
        "/ask",
        json={"question": "What is AI?"}
    )

    # Check that the API returns status code 200
    assert response.status_code == 200

    # Check that the returned answer matches the expected answer
    assert response.json()["answer"] == "AI is Artificial Intelligence."

    # Check that the database save function was called exactly once
    mock_save.assert_called_once()

def test_get_conversations():

    # Request the conversation history
    response = client.get("/conversations")

    # Check that the request was successful
    assert response.status_code == 200

    # Check that the response is a list
    assert isinstance(response.json(), list)