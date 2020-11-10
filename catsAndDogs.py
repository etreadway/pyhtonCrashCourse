def namePets(fileName):
    '''A script to read names off of a text file.'''
    try:
        with open(fileName, 'r') as fo:
            names = fo.readlines()
    except FileNotFoundError:
        print(fileName + ' could not be found.')
    else:
        for name in names:
            print(name.strip())

