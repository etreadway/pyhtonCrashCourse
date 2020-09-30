# checking to see if a number is a multiple of 10
num = input('Type any integer and I will tell you if it is a multiple of 10: ')

if int(num) % 10 == 0:
    print(num + ' is a multiple of 10.')
else:
    print(num + ' is NOT a multiple of 10.')