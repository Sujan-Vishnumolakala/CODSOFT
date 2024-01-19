import random

class SimpleChatBot:
    username = "Sujan"
    def __init__(self):
        self.exit_commands = ("quit", "exit", "bye")

    def greet(self):
        print("Hi there! I'm a simple chatbot. What's your name?")
        self.user_name = input("Your Name: ")
        print(f"Nice to meet you, {self.user_name}!")

    def chat(self):
        print("Let's chat! You can type 'quit' or 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in self.exit_commands:
                print("Chatbot: Goodbye! Have a nice day to you my friend.")
                break
            response = self.generate_response(user_input)
            print(f"Chatbot: {response}")

    def generate_response(self, user_input):
        if "how are you" in user_input:
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in user_input:
            return "I'm just a chatbot. You can call me ChatBot."
        elif "age" in user_input:
            return "I don't have an age. I'm a program."
        elif "joke" in user_input:
            return self.get_random_joke()
        elif "Hi" in user_input:
            return "Hi Sujan How can i assist you today ?" 
        else:
            return "I'm not sure how to respond to that as i am not trained up to that level.So kindly excuse me.Let's talk about something else."

    def get_random_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why did the computer go to therapy? Because it had too many bytes of emotional baggage."
        ]
        return random.choice(jokes)

if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.greet()
    chatbot.chat()
