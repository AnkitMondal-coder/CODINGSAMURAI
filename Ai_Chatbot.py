import random
import re
import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')

# Download punkt if not available
nltk.download('punkt', quiet=True)

# 1. Design Conversations (Define Pre-Defined Responses)
# We define responses for each potential user query

responses = {
    "hello": ["Hi there! How can I assist you today?", "Hello! What can I do for you?"],
    "hi": ["Hello! How can I help you?", "Hi! What would you like to know?"],
    "how are you": ["I'm just a bot, but I'm here to help you!", "I'm doing great, thanks for asking!"],
    "what's the weather like": ["I'm just a text-based bot and don't have access to real-time data. Sorry!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                       "Why did the coffee file a police report? It got mugged!"],
    "bye": ["Goodbye! Have a great day!", "See you later! Take care!"],
}

# 2. Preprocessing Function to Clean and Tokenize User Input
def preprocess_text(text):
    # Convert text to lowercase, remove punctuation, and tokenize
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)         # Tokenize the text
    return tokens

# 3. Chatbot Logic: Find the Best Response
def get_response(user_input):
    tokens = preprocess_text(user_input)
    for key in responses:
        # Check if any token in user input matches a response key
        if any(word in tokens for word in key.split()):
            return random.choice(responses[key])
    return "I'm not sure how to respond to that. Can you ask something else?"

# 4. Chatbot Interface (Main Program Loop)
def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Bot:", response)

# 5. Run the Chatbot
if __name__ == "__main__":
    chatbot()
