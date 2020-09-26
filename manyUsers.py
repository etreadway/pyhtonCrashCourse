users = {'ainstein':{
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie':{
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
        }

for userName, info in users.items():
    print('\nUsername: ' + userName)

    fullName = info['first'] + ' ' + info['last'] 
    location = info['location']

    print('Full Name: ' + fullName.title())
    print('Location: ' + location.title())
