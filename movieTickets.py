price = 0
count = 0
age = 0
ask = 'Would you like to purchase a movie ticket? (y/n): '
askAgain = 'Would you like to purchase another movie ticket? (y/n): '
askAge = 'Age?'


print('Welcome to Ticket Hub, your one stop online shop for movie tickets!!!')
print('\n')
print('*' * len('*Ticket Prices*'))
print('*Ticket Prices*')
print('*' * len('*Ticket Prices*'))
print('Adults/Teens 13 and up - $15')
print('Children 3 to 12 - $10')
print('Infants 2 and under - FREE')
print('\n')

flag = True
answer = input(ask)
if answer.lower() == 'n':
    flag = False
while flag == True:
    age = int(input(askAge))
    if age < 3:
        print('That will be Free!')
        count += 1
    elif age < 13:
        print('That will be $10')
        price += 10
        count += 1
    else:
        print('that will be $15')
        price += 15
        count += 1
    answer = input(askAgain)
    if answer.lower() == 'n':
        break
    else:
        continue

print('\nThank you for your purchase!')
print('You have purchased ' + str(count) + ' tickets.')
print('Your total is: $' + str(price))
#TODO:
# Build initial ask
# Build extra ask
# make sure to add to count and price
# print total number of movie tickets and price
