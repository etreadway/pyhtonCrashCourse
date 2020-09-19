# alienColor = 'red'
# alienColor = 'green'
alienColor = 'yellow'
points = 0

if alienColor == 'green':
    points = points + 5
    print('+5')
elif alienColor == 'yellow':
    points = points + 10
    print('+10')
elif alienColor == 'red':
    points == points + 15
    print('+15')