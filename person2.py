def buildPerson(firstName, lastName, age=''):
    '''Return a dictionary of information about a person.'''
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person
musician = buildPerson('jimi', 'hendrix', 27)
print(musician)
