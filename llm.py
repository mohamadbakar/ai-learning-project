import requests


# Send a question to the local Ollama model
def ask_ollama(question):

    try:
        response = requests.post(
            "http://host.docker.internal:11434/api/chat",
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

        # Raise an error if the HTTP request failed
        response.raise_for_status()

        answer = response.json()["message"]["content"]

        return answer

    except requests.exceptions.Timeout:
        raise RuntimeError("Ollama request timed out")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Could not connect to Ollama")

    except requests.exceptions.HTTPError:
        raise RuntimeError("Ollama returned an HTTP error")