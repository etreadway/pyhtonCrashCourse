usernames = ['eric', 'hannah', 'admin', 'doodle', 'burrow']
# usernames = []
# check to see if user is admin and then give a different message

if usernames:   # this is a check that usernames is not empty
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging in again.')
else:
    print('We need to find some users')