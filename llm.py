import requests


def ask_ollama(question):

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2",
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    answer = response.json()["message"]["content"]

    return answer