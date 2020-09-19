# Sorting cars alphabetically
cars = ['tesla', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Doing it in reverse
print('\n' + '-' * 20)
cars.sort(reverse=True)
print(cars)

# Sorting temporarily using sorted()
print('\n' + '-' * 20)
cars = ['tesla', 'audi', 'toyota', 'subaru']
print('Here is the og list:')
print(cars)
print('\nHere is the "sorted" list:')

print(sorted(cars))

print('\nHere is the og list again:')
print(cars)

# Printin the list in reverse order (Note: not reverse alpha)
print('\n' + '-' * 20)
print(cars)
cars.reverse()
print(cars)
cars.reverse() # <--- switching the order back

# Finding the length of a list
print('\n' + '-' * 20)
print('How many cars are in the list?')
print(len(cars))