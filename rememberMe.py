import json

def getStoredUsername():
    '''Get stored username if available.'''
    filename = 'username.json'
    try:
        with open(filename) as fo:
            username = json.load(fo)
    except FileNotFoundError:
        return None
    else:
        return username

def greetUser():
    '''Greet the user by name.'''
    username = getStoredUsername()
    if username:
        print('Welcome back, ' + username + '!')
    else:
        username = input('What is your name? ')
        filename = 'username.json'
        with open(filename, 'w') as fo:
            json.dump(username, fo)
            print('We will remimber you next time you come back, ' +
                  username + '!')
