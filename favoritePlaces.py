favoritePlaces = {'ltb': ['paris', 'san francisco', 'schlitterbahn'],
                'wife': ['bruge', 'chicago', 'bath'],
                'bug & burrow': ['the park', 'camp grandma', 'the pool'],
                }

for person, places in favoritePlaces.items():
    print('\n' + person.title() + '\'s Favorite Places')
    # making a line that conform to the length of the string
    print('-' * len(person.title() + '\'s Favorite Places'))
    # printing the places
    for place in places:
        print(place.title())