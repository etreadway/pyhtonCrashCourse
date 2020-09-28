# Dictionary of favorite numbers

favoriteNumbers = {'hannah': [13, 9],
                'elliot': [7],
                'shannon': [4, 15],
                'david': [7, 11],
                'mitch': [7],
                'nam': [3],
                'dalian': [4],
                'raven': [89, 5],
                }

for name, numbers in favoriteNumbers.items():
    print('\n')
    if len(numbers) < 1:
        print(name.title() + 'doesn\'t have a favorite number.')
    elif len(numbers) < 2:
        print(name.title() + '\'s Favorite Number')
        print('-' * len(name.title() + '\'s Favorite Number'))
        print(numbers)
    else:
        print(name.title() + '\'s Favorite Numbers')
        print('-' * len(name.title() + '\'s Favorite Numbers'))
        print(numbers)