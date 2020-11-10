def countWords(fileName):
    '''Count the approximate number of words in a file.'''
    # Use the codecs module so that we don't get a UnicodeDecodeError
    import codecs

    try:
        with codecs.open(fileName, 'r', encoding='utf-8',
                         errors='ignore') as fo:
            content = fo.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + fileName + ' does not exist.'
        print(msg)
    else:
        # Count the approximate number of words in the file
        words = content.split()
        numWords = len(words)
        print('The file ' + fileName + ' has about ' +
              str(numWords) + ' words.')

