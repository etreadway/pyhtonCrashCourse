import json

def greetUser():
    '''
    Load the username, if it has been stored previously.
    Otherwise, prompt for the username and store it.
    '''
    filename = 'username.json'
    try:
        with open(filename) as fo:
            username = json.load(fo)
    except FileNotFoundError:
        username = input('What is your name? ')
        with open(filename, 'w') as fo:
            json.dump(username, fo)
            print('We\'ll remember you when you come back, ' +
                  username + '!')
    else:
        print('Welcome back, ' + username + '!')
