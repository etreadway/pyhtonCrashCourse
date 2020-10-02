# list of sandwiches that need to be made
sandwichOrders = ['pb&j',
                  'turkey + cheese',
                  'chicken salad',
                  'pulled pork',
                  'knuckle',
                  ]

finishedSandwiches = []
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