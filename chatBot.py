responses = {
 "hi": ["Hello!", "Hi there!", "Hey!"],
 "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!"],
 "what is your name": ["You can call me ChatBot.", "I'm ChatBot."],
 "help": ["Sure, I can help you. What do you need help with?"],
 "weather": ["Sorry, I cannot provide weather information at the moment."],
 "bye": ["Goodbye!", "Bye! Take care."]
}

import random

def respond(user_input):
    for key in responses:
        if key == user_input:
            print(random.choice(responses[key]))
            return
    else:
        print('no')
            


def chat_bot():
    while True:
        user_input = input('You: ')

        user_input = user_input.lower()

        if user_input == 'quit':
            print('Goodbye')
            break
        respond(user_input)


chat_bot()