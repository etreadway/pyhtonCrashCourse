# example of if-elif-else statements

age = 12

# if age < 4:
#     print('admission is free')
# elif age < 18:
#     print('admission will be $5')
# else:
#     print('admission is $10')

# more concise way of doing things

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age >= 65:
    price = 5
else:
    price = 10

print('Your admission price will be $' + str(price) + '.')