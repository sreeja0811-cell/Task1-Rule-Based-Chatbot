print("=" * 40)
print("🤖 AI Rule-Based Chatbot")
print("Type 'bye' to exit")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I assist you today?")

    elif "name" in user:
        print("Bot: My name is AI Chatbot.")

    elif "healthcare" in user:
        print("Bot: AI can help healthcare professionals make better decisions and improve patient care.")

    elif "how are you" in user:
        print("Bot: I am doing great. Thanks for asking!")

    elif "python" in user:
        print("Bot: Python is a popular language used for AI, Machine Learning, and Web Development.")

    elif "ai" in user:
        print("Bot: Artificial Intelligence enables machines to simulate human intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI that learns patterns from data.")

    elif "react" in user:
        print("Bot: React is a JavaScript library used for building user interfaces.")

    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")