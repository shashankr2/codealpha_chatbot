import random
import re
import time

# Define response patterns
response_dict = {
    ('hello', 'hi', 'hey'): [
        "Hello! How can I help you?",
        "Hi there! What's on your mind?",
        "Hey! What can I do for you?"
    ],
    ('bye', 'goodbye', 'exit'): [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Come back anytime!"
    ],
    ('how are you', 'how you doing'): [
        "I'm just a program, but I'm functioning well!",
        "I don't have feelings, but thanks for asking!",
        "All systems go! How can I assist you?"
    ],
    ('your name', 'who are you'): [
        "I'm ChatBot 1.0, your digital assistant!",
        "You can call me CB, your friendly chatbot!",
        "I'm a basic chatbot here to help you!"
    ],
    ('help', 'support'): [
        "I can help with basic conversations. Try asking me questions!",
        "I'm here to chat! Ask me about anything simple."
    ],
    ('time', 'current time'): [
        f"The current time is {time.strftime('%H:%M')}",
        f"Right now it's {time.strftime('%I:%M %p')}"
    ],
    ('date', 'today\'s date'): [
        f"Today's date is {time.strftime('%Y-%m-%d')}",
        f"It's {time.strftime('%A, %B %d, %Y')}"
    ],
    ('thank you', 'thanks'): [
        "You're welcome!",
        "My pleasure!",
        "Glad I could help!"
    ]
}

# Default responses
default_responses = [
    "Interesting! Could you explain that differently?",
    "I'm still learning. Could you rephrase that?",
    "Let's talk about something else. What's on your mind?",
    "Hmm, I'm not sure I understand. Can you ask another way?"
]

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for matches in response patterns
    for patterns, responses in response_dict.items():
        if any(re.search(r'\b' + pattern + r'\b', user_input) for pattern in patterns):
            return random.choice(responses)
    
    # Check for specific patterns
    if re.search(r'weather', user_input):
        return "I can't check real weather, but every day is sunny in the digital world!"
    
    if re.search(r'(joke|funny)', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    # Default response if no matches
    return random.choice(default_responses)

def chat():
    print("ChatBot 1.0: Hi! I'm your basic chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit']):
            print(random.choice(response_dict[('bye', 'goodbye', 'exit')]))
            break
            
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()