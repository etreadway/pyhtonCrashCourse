dreamVacation = {}
askName = 'What is your name? '
askVaca = 'What is your dream vacation spot? '
askAgain = 'Would you like to make another entry? (y/n) '

# Build a dict of names and responses
while True:
    name = input(askName)
    location = input(askVaca)
    dreamVacation[name] = location
    again = input(askAgain)
    if again.lower() == 'n' or again.lower() == 'no':
        break

# print each key/value in a sentince from dict
for name, location in dreamVacation.items():
    print('\n' + name.title() +
    ' would like to go to ' +
    location.title() +
    '.')


