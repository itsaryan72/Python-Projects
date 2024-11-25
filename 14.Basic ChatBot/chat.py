#Basic Chatbot:Implement a simple rule-based chatbot that can respond to user inputs with pre-defined answers.

def chatBot():

    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! What do you need help with?",
        "how are you": "I'm just a program, but I'm functioning as expected!",
        "what is your name": "I'm a simple chatbot created by you!",
        "bye": "Goodbye! Have a great day!",
    }

    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit the chat.")


    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        response = responses.get(user_input, "I'm sorry, I didn't understand that.")
        print(f"Chatbot: {response}")


chatBot()