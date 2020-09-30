# writing a prompt in a veriable to pass into input()
prompt = 'If you tell us who you are, we can persionalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
age = input('How old are you? ')
age = int(age)
print('\nHello, ' + name.title() + '!')
if age == 1:
    print('You are ' + str(age) + ' year old.')
else:
    print('You are ' + str(age) + ' years old')