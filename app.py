def answer_question(question):

    if question == "What is AI?":
        return "AI means Artificial Intelligence."

    elif question == "What is Python?":
        return "Python is a programming language."

    else:
        return "I don't know this question yet."


user_question = input("Ask me something: ")

response = answer_question(user_question)

print(response)