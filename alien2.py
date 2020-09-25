# this is an empty list for storing aliens
# populating a list with dictionaries

aliens =[]

for alien in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# counting how many aliens were created
# print(len(aliens))
# printing the first 5 aliens to make sure they have the right elements
for alien in aliens[:5]:
    print(alien)
