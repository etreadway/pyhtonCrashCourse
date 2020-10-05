cindy = {'type': 'dog',
         'owner': 'me',
         'name': 'cindy',
         }
tiny = {'type': 'cat',
        'owner': 'dad',
        'name': 'tiny',
        }
sherly = {'type': 'cat',
          'owner': 'mom',
          'name': 'sherly',
          }
blacky = {'type': 'cat',
        'owner': 'mom',
        'name': 'blacky',
        }
janey = {'type': 'cat',
        'owner': 'mom',
        'name': 'janey',
        }
shane = {'type': 'dog',
        'owner': 'mom',
        'name': 'shane',
        }
daphnie = {'type': 'dog',
        'owner': 'mom',
        'name': 'daphnie',
        }
doodle = {'type': 'dog',
        'owner': 'wife & me',
        'name': 'doodle',
        }
burrow = {'type': 'dog',
        'owner': 'wife & me',
        'name': 'burrow',
        }

pets = [cindy, tiny, sherly, blacky, janey, shane, daphnie, doodle, burrow]

for pet in pets:
        print('\n' + pet['name'].title())
        print('-' * 20)
        print('Type: ' + pet['type'].title())
        print('Owner: ' + pet['owner'].title())

# building a list from the dictionaries
animals =[]
for pet in pets:
        animals.append(pet['type'])

print('\n')
print(animals)
# removing cats from the list 
while 'cat' in animals:
        animals.remove('cat')

print(animals)

# using a function to print info about a pet
def describePet(name, type='dog'):
        '''Display information about a pet.'''
        print('\nI have a ' + type + '.')
        print('My ' + type + '\'s name is  ' + name.title() + '.')

# keyword argument
describePet(type='hamster', name='harry')
# positional argument
describePet('janie', 'cat')
# default value
describePet(name='cindy')