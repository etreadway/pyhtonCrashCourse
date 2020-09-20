# Dictionary of favorite numbers

favoriteNumbers = {'hannah': 13,
                   'elliot': 7,
                   'shannon': 4,
                   'david': 7,
                   'mitch': 7,
                   'nam': 3,
                   'dalian': 4,
                   'raven': 89,}

# building a loop to print all keys
for name in favoriteNumbers:
    print('\n'
          + name.title()
          + '\'s favorite number is '
          + str(favoriteNumbers[name])
          + '.')