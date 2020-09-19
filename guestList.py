# this is for sending out invites to the guests on the list
guestList = ['hannah', 'elliot', 'jordan']

# making the invites
for guest in guestList:
    print('To ' + guest.title() + ',\nYou have been invited to movie night on friday. Bring snacks, drinks, or anything else you want.\n')

# Elliot cant come so I got to """pop""" him off the list and print a new one
print('-' * 20)
poppedGuest = guestList.pop(1)
print('It would seem that ' + poppedGuest.title() + ' can\'t make it because he lives in Portland or something?')
guestList.insert(0, 'doug')
print('On the brighter side it seems that ' + guestList[0].title() + ' will be making an appearance.')
print('\n')

for guest in guestList:
    print('To ' + guest.title() + ',\nYou have been invited to movie night on friday. Bring snacks, drinks, or anything else you want.\n')

# inviting even more people by """inserting""" them into the list
print('-' * 20)
print('Guess what y\'all, I found an old couch on the side of the road! so we can invite a few more people! Put the word out.\n')
guestList.insert(0, 'bryan')
guestList.insert(2, 'andy')
guestList.append('boogle')

for guest in guestList:
    print('To ' + guest.title() + ',\nYou have been invited to movie night on friday. Bring snacks, drinks, or anything else you want.\n')

# Uninviting guests by popping them of the list
print('-' * 20)
print('Fuck.... my bad y\'all... the couch had bugs. We got it out before they infested anything in the house\n'
      'but we dont have room for everyone. so we\'ve got to take some of you off the list.\n')

while len(guestList) > 3:
    uninvited = guestList.pop(-1)
    print('Yo ' + uninvited.title() + '... sorry to be a dick but we don\'t have room anymore. Lets kick it soon though.\n')

for guest in guestList:
    print('To ' + guest.title() + ',\nYou have been invited to movie night on friday. Bring snacks, drinks, or anything else you want.\n')

print('The number of people coming to movie night is ' + str(len(guestList)) + '.')
# Clearing the list
print('-' * 20)
while len(guestList) >0:
    del guestList[0]
print(guestList)