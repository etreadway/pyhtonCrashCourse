# this is how you use slices
players = ['charles', 'martina', 'michael', 'florance', 'eli']
print(players[0:3])
print(players[1:4])

# start slice at beginning
print(players[:4])

# end slice at end of list
print(players[2:])

# begin slice 3 from the end regardless of length
print(players[-3:])

# using loops to print slices
print('Here are the first three players on my team:')
for player in players:
    print(player.title())

# slices
print('The first three items on the list are:')
for player in players[:3]:
    print(player)
print('\nThree items from the middle of the list are:')
for player in players[1:4]:
    print(player)
print('\nThe last three items in the list are:')
for player in players[-3:]:
    print(player)