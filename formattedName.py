def formattedName(firstName, lastName, middleName=''):
    '''Return a full name, neatly formatted.'''
    if middleName:
        fullName = firstName + ' '\
                   + middleName + ' '\
                   + lastName
    else:
        fullName = firstName + ' ' + lastName
    return fullName.title()

musician = formattedName('jimi', 'hendrix')
print(musician)
musician = formattedName('john', 'hooker', 'lee')
print(musician)
