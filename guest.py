fileName = 'guest.txt'

fo = open(fileName, 'a')
name = input('What is your name? ')
if name.title() in fo:
    print('Looks like you\'ve already signed the guest book.')
else:
    fo.write(name.title() + '\n')
    print('Thanks for signing the guest book!')
fo.close()