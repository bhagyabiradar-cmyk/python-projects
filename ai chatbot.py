import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm doing great!", "I'm fine, thank you!"],
    "what is your name": ["I'm a Python AI chatbot."],
    "bye": ["Goodbye!", "See you later!"]
}

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("🤖 Chatbot:", random.choice(responses["bye"]))
        break

    found = False

    for question in responses:
        if question in user:
            print("🤖 Chatbot:", random.choice(responses[question]))
            found = True
            break

    if not found:
        print("🤖 Chatbot: Sorry, I don't understand that.")