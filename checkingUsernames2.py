currentUsers = ['LTB', 'KJT', 'damus', 'etread72', 'estreadway']
newUsers = ['hannah', 'eric', 'LTB', 'kjt', 'doodle', 'burrow']

for user in newUsers:
    if user in currentUsers:
        print('Please pick a different username, ' + user + ' is already taken')
    else:
        print(user + ' is available.')