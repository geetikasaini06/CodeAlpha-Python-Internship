
def get_response(message):
    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message in ["your name", "what is your name"]:
        return "I'm a basic Python chatbot."

    elif message == "help":
        return "Sure! How can I help you?"

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that yet."


def start_chatbot():
    print("Welcome to Python Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_message = input("You: ").lower().strip()

        if user_message == "":
            print("Bot: Please enter a message.")
            continue

        response = get_response(user_message)
        print("Bot:", response)

        if user_message == "bye":
            break


start_chatbot()
