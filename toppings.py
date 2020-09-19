# Using for loops with multiple lists

availableToppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pinapple', 'extra cheese']

requestedToppings = ['mushrooms', 'onions', 'extra cheese']

for topping in requestedToppings:
    if topping in availableToppings:
        print('Adding ' + topping + '.')
    else:
        print('Sorry, we don\'t have ' + topping + '.')

print('\nFinished with your pizza!')