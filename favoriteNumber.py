import json

def getNumber():
    '''A simple function to collect and save the users favorite number.'''
    favNum = input('What is your favorite number?')
    filename = "favoriteNumber.json"
    with open(filename, 'w') as fo:
        json.dump(favNum, fo)
    print('I will remember that your favorite number is ' + favNum + '.')

def sayNumber():
    '''A simple function for retrieving the users favorite number.'''
    filename = 'favoriteNumber.json'
    try:
        with open(filename) as fo:
            favNum = json.load(fo)
    except FileNotFoundError:
        return None
    else:
        return favNum


def favoriteNumber():
    '''Tell the user the stored favorite number.'''
    favNum = sayNumber()
    if favNum:
        print('Your favorite number is ' + favNum + '!')
    else:
        getNumber()

favoriteNumber()