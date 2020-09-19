# These are my favorite pizzas

favoritePizzas = ['deep dish pizza', 'pineapple pizza', 'stuffed crust pizza']

for pizza in favoritePizzas:
    print('One of my favorite pizzas to eat is ' + pizza.title() + '.\n')

print('Pizza is good but too much of a good thing...')

# making a copy with slices
wifePizza = favoritePizzas[:]
favoritePizzas.append('pepperoni pizza')
wifePizza.append('pepperoni and black olive pizza')

# printing to prove the lists are different
print('My favorite pizzas are:')
for pizza in favoritePizzas:
    print(pizza)

print('\nMy wife\'s favorite pizzas are:')
for pizza in wifePizza:
    print(pizza)