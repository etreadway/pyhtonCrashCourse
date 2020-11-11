def commonWord(fileName, word):
    '''
    A simple function for counting the words in a text file.
    Currently, the text file must be in the same folder as this.
    '''

    # Codecs is used to avoid unicode errors
    import codecs
    try:
        with codecs.open(fileName, 'r', encoding='utf-8',
                     errors='ignore') as fo:
            content = fo.read()
    except FileNotFoundError:
        print('Could not find ' + fileName + '.')
        print('Please make sure the file is in the same '
              'folder as this program')
    else:
        # content.lower() is used so that the count is case insensitive
        num = content.lower().count(word)
        print('The word "' + word + '" appears ' +
              str(num) + ' times.')


print('Welcome to Low Tier Beer\'s Word Counter!')

while True:
    f = input('What file would you like to check? ')
    w = input('What word would you like to count? ')

    commonWord(f, w)

    check = input('Would you like to check another word? (Y/n) ')
    if check.lower() == 'n':
        break