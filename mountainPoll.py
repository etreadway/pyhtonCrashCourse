responses = {}

# set a flag to indicate that polling is active.
pollingActive = True

while pollingActive:
    # prompt for the person's name and response.
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # store the response in the dictionary.
    responses[name] = response

    # find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/ no)')
    if repeat.lower() == 'no':
        pollingActive = False

# polling is complete, show the results
print('\n---Pool Results---')
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() + '.')