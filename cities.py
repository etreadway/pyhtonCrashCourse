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