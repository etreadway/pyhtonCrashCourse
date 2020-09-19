# # making a dictionary

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# ---------------------------------------------------------------

# # printing from a dict

# newPoints = alien_0['points']
# print('You just earned ' + str(newPoints) +' points!!!')
#
# ---------------------------------------------------------------

# # adding to a dict

# print(alien_0)
#
# alien_0['xPosition'] = 0
# alien_0['yPosition'] = 25
# print(alien_0)
#
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# -----------------------------------------------------------------

# # modifying a dict

# alien = {'color': 'green'}
# print('The alien is ' + alien['color'] + '.')
#
# alien['color'] = 'yellow'
# print('The alien is now ' + alien['color'])

# ------------------------------------------------------------------

# # applied moding a dict
alien = {'xPosition': 0, 'yPosition': 25, 'speed': 'medium'}
print('Origional x-position: ' + str(alien['xPosition']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    # This must be the fast alien
    x_increment = 3

# This new position is the old position plus the increment.
alien['xPosition'] = alien['xPosition'] + x_increment

print('New x-position: ' + str(alien['xPosition']))