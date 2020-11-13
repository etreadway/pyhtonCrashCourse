from nameFunction import getFormattedName

print('Enter "q" to quit at any time.')
while True:
    first = input('\nPlease give me your first name: ')
    if first == 'q':
        break
    last = input('Please give me a last name: ')
    if last == 'q':
        break

    formattedName = getFormattedName(first, last)
    print('\tNeatly formatted name: ' + formattedName + '.')