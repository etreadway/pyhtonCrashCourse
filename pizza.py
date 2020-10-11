# Using an arbitrary number of keyword arguments

def makePizza(size, *toppings):
    '''Summarize the pizza we are about to make.'''
    print('\nMaking a ' + str(size) +
        '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
makePizza(16, 'pepperoni')
makePizza(12, 'mushrooms', 'green peppers', 'extra cheese')
