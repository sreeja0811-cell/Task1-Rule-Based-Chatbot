import datetime

user_name = ""
question_count = 0

print("="*60)
print("🤖 SMART AI ASSISTANT CHATBOT")
print("="*60)

user_name = input("👤 Enter your name: ")

print(f"\n🤖 Hello {user_name}! Welcome to the AI Assistant.")
print("Type 'help' for available commands.")
print("Type 'bye' to exit.")

while True:

    user = input(f"\n{user_name}: ").lower().strip()
    question_count += 1

    # Greetings
    if user in ["hello","hi","hey"]:
        print(f"🤖 Hello {user_name}! How can I help you today?")

    # About chatbot
    elif "name" in user:
        print("🤖 I am Smart AI Assistant Chatbot.")

    # AI
    elif "ai" in user:
        print("🤖 Artificial Intelligence enables machines to simulate human intelligence.")

    # Machine Learning
    elif "machine learning" in user:
        print("🤖 Machine Learning is a subset of AI that learns patterns from data.")

    # Python
    elif "python" in user:
        print("🤖 Python is widely used in AI, Machine Learning, Data Science and Web Development.")

    # React
    elif "react" in user:
        print("🤖 React is a JavaScript library used for building modern user interfaces.")

    # Healthcare
    elif "healthcare" in user:
        print("🤖 AI in healthcare helps doctors with diagnosis, decision support and patient care.")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"🤖 Current Time: {current_time}")

    # Date
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"🤖 Today's Date: {current_date}")

    # Calculator
    elif user.startswith("calc"):

        try:
            expression = user.replace("calc","")
            result = eval(expression)
            print(f"🤖 Result = {result}")
        except:
            print("🤖 Invalid Expression")

    # Positive sentiment
    elif any(word in user for word in ["good","great","awesome","happy"]):
        print("🤖 That's wonderful to hear! 😊")

    # Negative sentiment
    elif any(word in user for word in ["sad","bad","upset","angry"]):
        print("🤖 I'm sorry to hear that. Hope things improve soon. ❤️")

    # Statistics
    elif "stats" in user:
        print(f"🤖 Total Questions Asked: {question_count}")

    # Help Menu
    elif "help" in user:

        print("\n📋 AVAILABLE COMMANDS")
        print("- hello")
        print("- what is ai")
        print("- what is machine learning")
        print("- what is python")
        print("- what is react")
        print("- healthcare")
        print("- date")
        print("- time")
        print("- calc 5+10")
        print("- stats")
        print("- bye")

    # Thanks
    elif "thank" in user:
        print("🤖 You're welcome!")

    # Exit
    elif user == "bye":
        print(f"🤖 Goodbye {user_name}! Have a great day.")
        break

    else:
        print("🤖 Sorry, I don't understand. Type 'help' for commands.")
