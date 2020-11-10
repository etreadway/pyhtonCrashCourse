def commonWord(fileName, word):
    import codecs
    try:
        with codecs.open(fileName, 'r', encoding='utf-8',
                     errors='ignore') as fo:
            content = fo.read()
    except FileNotFoundError:
        print('Could not find ' + fileName)
    else:
        num = content.count(word)
        print('The word ' + word + ' appears ' +
              str(num) + ' times.')

commonWord('alice.txt', 'a')