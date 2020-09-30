cars = ['tesla', 'audi', 'toyota', 'subaru']

rentRequest = input('What kind of car would you like to rent?\n')
rentRequest = rentRequest.lower()

print('Let me see if we have a ' + rentRequest.title() + 'you can rent...')
print('*' * 20)
if rentRequest in cars:
    print('Looks like we have a ' + rentRequest.title() + ' in stock.')
else:
    print('Sorry, we don\'t have any ' + rentRequest.title() + '.')