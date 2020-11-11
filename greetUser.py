import json
filename = 'username.json'

with open(filename) as fo:
    username = json.load(fo)
    print('Welcome back, ' + username + '!')