import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet

# Function to replace words with synonyms
def replace_synonyms(response):
    words = response.split()
    replaced_words = []
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            synonym = synsets[0].lemmas()[0].name()
            replaced_words.append(synonym)
        else:
            replaced_words.append(word)
    return ' '.join(replaced_words)

# Define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot."]
    ],
    [
        r"what do you like to do\?",
        ["I enjoy chatting with people and helping them."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"where are you from\?",
        ["I'm a virtual assistant, so I don't have a physical location."]
    ],
    [
        r"what is the meaning of life\?",
        ["The meaning of life can vary for each person, but it's often about finding happiness and fulfillment."]
    ],
    [
        r"how are you\??",
        ["I'm doing well, thank you! How about you?"]
    ],
    [
        r"are you ok\??",
        ["I'm just a computer program, so I don't have feelings, but thank you for asking!"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please repeat?"]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Main loop
print("Hello! I'm a simple chatbot. You can start chatting with me. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot.respond(user_input)
    response = replace_synonyms(response)
    print("Bot:", response)
