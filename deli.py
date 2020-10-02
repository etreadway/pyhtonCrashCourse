# list of sandwiches that need to be made
sandwichOrders = ['pb&j',
                'pastrami',
                'turkey + cheese',
                'chicken salad',
                'pastrami',
                'pulled pork',
                'knuckle',
                'pastrami',
                ]
finishedSandwiches = []

# Telling customers the deli is out fo pastrami and removing those orders
print('The Deli is all out of pastrami!')
while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')
# moving each sandwich to the finished list when they are made
while sandwichOrders:
    currentSandwich = sandwichOrders.pop()
    print('making your ' + currentSandwich + ' sandwich.')
    finishedSandwiches.append(currentSandwich)

# Telling the costomer their order is ready
print('\nYour order is finished')

# Building a proper sentence structure using the list
orderSentence = 'Come get your '
for sandwich in finishedSandwiches[0:-1]:
    orderSentence += sandwich + ', '
orderSentence += 'and ' + finishedSandwiches[-1] + ' sandwiches.'
print(orderSentence)