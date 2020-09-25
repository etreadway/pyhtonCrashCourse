# Storing info about a pizza being ordered (lists in dictionary)

pizza = {
    'crust': 'thick',
    'toppings': ['pineapple', 'pepperoni', 'extra cheese'],
    }
# Summarizing the order
print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
      'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)