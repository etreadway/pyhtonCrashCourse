fileName = 'guestBook.txt'
fo = open(fileName, 'r+')

check = ''
while check.lower() != 'n':
    name = input('What is your name? ')
    if name.title() in fo:
        print('Looks like you\'ve already signed the guest book.')
    else:
        fo.write(name.title() + '\n')
        print('Thanks for signing the guest book!')
    check = input('Whould you like to put another name in the guestbook? (y/n)')
fo.close()