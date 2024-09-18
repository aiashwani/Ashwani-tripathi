def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hello! How can I help you?",
        "helo": "Hello! How can I help you?",
        "bye": "Goodbye! Have a nice day!",
        "how are you": "I'm just a bunch of code, but I'm doing well!. What about you",
        "what's your name":"I'm a simple chatbot created to assist you!",
        "help":"Sure! What do you need help with?",
        "thank you":"You're welcome! If you have any more questions, feel free to ask.",
        "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "weather":"I can't check the weather, but I hope it's nice where you are!",
        "your favorite color":"I don't have a favorite color, but I hear blue is quite popular!",
        "who created you": "I was created by developers who love programming!",
        "love" : "Love is a beautiful thing! What does it mean to you?",
        "do you have feelings":"I don't have feelings like humans do, but I'm here to support you!",

    }
    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    return "Sorry, I don't understand that."


while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Chatbot:", chatbot_response(user_input))
