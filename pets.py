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