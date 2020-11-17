def getFormattedName(first, last, middle=''):
    '''Geretate a neatly formatted full name.'''
    if middle:
        fullName = first + ' ' + middle + ' ' + last
    else:
        fullName = first + ' ' + last
    return fullName.title()