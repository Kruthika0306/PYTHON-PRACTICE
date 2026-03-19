print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hi there!")
    elif user == "how are you":
        print("Chatbot: I'm just code, but I'm good ")
    elif user == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: I don't understand")
