cities = {'athens':
            {'country': 'greece', 'population': '~3.1m', 'fun fact': 'Birthplace of democracy'},
        'venice':
            {'country': 'italy', 'population': '~262k', 'fun fact': 'No roads... Vin Diesel would hate it'},
        'florance':
            {'country': 'italy', 'population': '~328k', 'fun fact': 'Birthplace of the Renaissance'}
        }

for city, info in cities.items():
    print('\n' + '*' * (len(city.title()) + 2))
    print('*' + city.title() + '*')
    print('*' * (len(city.title()) + 2))
    location = info['country']
    pop = info['population']
    funFact = info['fun fact']
    print('Location: ' + location.title())
    print('Population: ' + pop)
    print('Fun fact: ' + funFact)

msg = '\nPlease enter the name of a city you think would be nice to visit: '

while True:
    city = input(msg)

    if city.lower() == 'quit':
        break
    elif city.lower() in cities.keys():
        print('Ive been to ' + city.title() + ' and it\'s wonderful.')
    else:
        print('I\'d love to go to ' + city.title() + '!')
    print('Enter "quit" if you are finished or enter another city.')