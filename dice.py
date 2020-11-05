# Importing random
import random

# Creating a class for dice
class Die():
    '''A class for simulating a die.'''

    def __init__(self, sides):
        '''Initialize basic die info'''
        self.sides = sides

    def rollDie(self):
        '''Simulates a die role.'''
        x = random.randint(1, self.sides)
        print('You have rolled a ' + str(x) + '!')

# Creating a 6 sided die and rolling it 10 times
print('d6')
d6 = Die(6)
for roll in range(0, 10):
    d6.rollDie()

# Creating a 10 sided die and rolling it 10 times
print('d10')
d10 = Die(10)
for roll in range(0, 10):
    d10.rollDie()

# Creating a 20 sided die and rolling it 10 times
print('d20')
d20 = Die(20)
for roll in range(0, 10):
    d20.rollDie()