prompt = 'Tell me something, and I will repeat it back to you: '

active = True
while active:
    message = input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(message)
        print('\nEnter "quit" to end the program')