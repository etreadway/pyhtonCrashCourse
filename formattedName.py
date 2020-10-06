def formattedName(firstName, lastName):
    '''Return a full name, neatly formatted.'''
    fullName = firstName + ' ' + lastName
    return fullName.title()

musician = formattedName('jimi', 'hendrix')
print(musician)