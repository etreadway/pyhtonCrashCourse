counter = input('How many people are in your dinner group? ')
counter = int(counter)

if counter > 8:
    print('You will need to wait for a table.')
elif counter == 0:
    print('Find a table anywhere in the null section.')
elif counter < 0:
    print('We don\'t need that kind of negativity in our establishment.')
    print('Please leave!')
else:
    print('Your table is ready.')