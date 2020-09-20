# example of printing from a dictionary

wife = {'first name': 'boo',
        'last name': 'berry',
        'age': 30,
        'city': 'h-town'}
for key in wife:
    print(key.title() + ': ' + str(wife[key]).title())