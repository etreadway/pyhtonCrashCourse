msg = '\nWhat topping would you like to add? (type "done" to finish your order)'
toppings = []
newTopping = ''

while True:
    newTopping = input(msg)
    if newTopping.lower() == 'done':
        break
    print(newTopping.title() + ' has been added to your order.')
    toppings.append(newTopping.lower())

print('\n\nThank you for your order!')
print('Your pizza toppings are:')
for topping in toppings:
    print(topping.title())
print('Your pizza will be ready soon')