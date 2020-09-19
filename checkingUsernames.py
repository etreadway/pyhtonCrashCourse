currentUsers = ['LTB', 'KJT', 'damus', 'etread72', 'estreadway']
newUsers = ['hannah', 'eric', 'ltb', 'kjt', 'doodle', 'burrow']


# if user.lower() in ():
#     print('Please pick a different username, ' + user + ' is already taken')
# else:
#     print(user + ' is available.')



# creating two lowercase lists to check
lowerCurrent = []
for user in currentUsers:
    lowerCurrent.append(user.lower())

lowerNew = []
for user in newUsers:
    lowerNew.append(user.lower())

for user in lowerNew:
    if user in lowerCurrent:
        print('try again')
    else:
        print('g2g')

# for user in newUsers:
#     if user.lower() in (current.lower() for current in currentUsers):
#         print('try again')
#     else:
#         print('good to go')

# for user in newUsers:
#     for current in currentUsers:
#         if user.lower() in current.lower():
#             print('try again')
#         else:
#             print('good to go')