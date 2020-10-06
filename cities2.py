# make a  function that will print the name of a city and the country that it's in
cities = {'athens':
            {'country': 'greece', 'population': '~3.1m', 'fun fact': 'Birthplace of democracy'},
        'venice':
            {'country': 'italy', 'population': '~262k', 'fun fact': 'No roads... Vin Diesel would hate it'},
        'florance':
            {'country': 'italy', 'population': '~328k', 'fun fact': 'Birthplace of the Renaissance'}
        }

def describeCity(city = 'reykjavik', country = 'iceland'):
    print(city.title() +
          'is located in ' +
          country.title() +
          '.')

describeCity('athens', 'greece')
describeCity('venice', 'italy')
describeCity('florance', 'italy')
describeCity()