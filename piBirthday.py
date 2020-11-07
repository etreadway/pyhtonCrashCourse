fileName = 'pi_million_digits.txt'

with open(fileName) as txt:
    lines = txt.readlines()

piString = ''
for line in lines:
    piString += line.strip()

check = ''
while check.capitalize() != 'N':
    birthday = input('Enter your birthday (mmddyy): ') 

    if birthday in piString:
        print('Your birthday appears in the first million digits of pi!')
    else:
        print('Your birthday is NOT in the first million digits of py.')
    check = input('Whould you like to check another birthday? (y/n): ')