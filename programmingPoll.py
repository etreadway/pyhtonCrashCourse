fN = 'programmingPoll.txt'
fo = open(fN, 'a+')

check = ''
while check.lower() != 'n':
    reason = input('Why do you love programming? ')
    fo.write(reason + '\n')
    check = input('Whould you like to give another reason? (Y/n) ')
fo.close()