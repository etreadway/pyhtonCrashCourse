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

def getNewUsername():
    '''Prompt for a new username.'''
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as fo:
        json.dump(username, fo)
    return username

def greetUser():
    '''Greet the user by name.'''
    username = getStoredUsername()
    if username:
        print('You are currently logged in as ' + username + '.')
        logout = input('Is this correct? (Y/n) ')
        if logout.lower() == 'n':
            username = getNewUsername()
            print('We will remember you next time you come back, ' +
                  username + '!')
        else:
            print('Welcome back, ' + username + '!')
    else:
        username = getNewUsername()
        print('We will remember you next time you come back, ' +
              username + '!')
greetUser()