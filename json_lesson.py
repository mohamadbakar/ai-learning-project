import json

data = {
    "question": "What is AI?",
    "answer": "AI means Artificial Intelligence."
}

# Convert Python dictionary to JSON text
json_text = json.dumps(data, indent=4)

# Convert JSON text back to Python dictionary
loaded_data = json.loads(json_text)

print(loaded_data["question"])
print(loaded_data["answer"])