# Start with a list of users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmedUsers = ['alice', 'brian', 'candace']
confirmedUsers = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()

    print('Verifying user: ' + currentUser.title())
    confirmedUsers.append(currentUser)

# display all confirmed users.
print('\nThe following users have been confirmed:')
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())