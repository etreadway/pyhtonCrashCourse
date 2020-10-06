# # writing a prompt in a variable to pass into input()
# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += '\nWhat is your first name? '
#
# name = input(prompt)
# age = input('How old are you? ')
# age = int(age)
# print('\nHello, ' + name.title() + '!')
# if age == 1:
#     print('You are ' + str(age) + ' year old.')
# else:
#     print('You are ' + str(age) + ' years old')

# # using a function to greet different users
# def greetUser(username):
#     '''Display a simple greeting.'''
#     print('Hello, ' + username.title() + '!')
#
# greetUser('jesse')

def getFormattedName(firstName, lastName):
    '''Return a full name, neatly formatted.'''
    fullName = firstName + ' ' + lastName
    return fullName.title()

# this is an infinite loop!
while True:
    print('\nPlease tell me your name:')
    print('(Enter \'q\' at any time to quit)')
    fName = input('First name: ')
    if fName == 'q':
        break
    lName = input('Last name: ')
    if lName == 'q':
        break

    formattedName = getFormattedName(fName, lName)
    print('\nHello, ' + formattedName + '!')