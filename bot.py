import random
import re
responses = {
    r"\bhello\b": "Hello! How can I assist you?",
    r"\bhow are you\b": "I'm just a chatbot, but I'm here to help!",
    r"\bbye\b": "Goodbye! Have a great day!",
    r"\bhelp\b": "I'm here to help you. Feel free to ask me anything.",
    r"\bhow does this chatbot work\b": "This chatbot works by matching your input to a set of predefined rules or patterns and generating appropriate responses. You can ask me anything from the prompts mentioned here and I’ll give you a response accordingly.",
    r"\bbook recommendation\b": "Sure, I can help you with that. What genre are you interested in?",
    r"\bcheck the status of my order\b": "You can check the status of your order by entering your order number and email address here order status page.",
    r"\bcancel subscription\b":"We’re sorry to hear that you want to cancel your subscription. To cancel your subscription, please follow these steps cancellation instructions.",
    r"\btell me a joke\b":"Sure, I can tell you a joke. Here’s one: What do you call a fish that wears a bowtie? Sofishticated.",
    r".*": "I'm sorry, I didn't understand that."
}


def get_response(user_input):
    user_input = user_input.lower()
    
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
        
    
def main():
    greetings = [
    "Hello! How can I assist you?",
    "Hi there! What can I do for you?",
    "Greetings! How may I help you?"]
    
    print(random.choice(greetings))
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit" or user_input.lower() == "bye"  :
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
