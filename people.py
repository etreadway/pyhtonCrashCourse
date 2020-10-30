
people = {'wife':{
            'first': 'boo',
            'last': 'berry',
            'age': 30,
            'city': 'h-town',
            },
        'medium dog':{
            'first': 'bug',
            'last': 'friend',
            'age': 5,
            'city': 'h-town',
            },
        'small dog':{
            'first': 'tiny',
            'last': 'pup',
            'age': 2,
            'city': 'h-town',
            },
        }

for person, info in people.items():
    print('\n' + '-' * 20)
    print(person.title())
    print('-' * 20)

    fullName = info['first'] + ' ' + info['last']
    print('Name: ' + fullName)
    print('Age: ' + str(info['age']))
    print('City: ' + info['city'].title())
