sandwichOrders = ['pb&j',
                  'turkey + cheese',
                  'chicken salad',
                  'pulled pork',
                  'knuckle',
                  ]

finishedSandwiches = []

while sandwichOrders:
    currentSandwich = sandwichOrders.pop()
    print('making your ' + currentSandwich + ' sandwich.')

    finishedSandwiches.append(currentSandwich)

print('\nYour order is finished')
orderSentence = 'Come get your '
for sandwich in finishedSandwiches[0:-1]:
    orderSentence += sandwich + ', '

orderSentence += 'and ' + finishedSandwiches[-1] + ' sandwiches.'
print(orderSentence)