# creating a list
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
# appending a list
motorcycles.append('Ducati')
print(motorcycles)

# using the pop() method
print('-' * 20)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print('-' * 20)
motorcycles = ['honda', 'yamaha', 'suzuki']
lastOwned = motorcycles.pop()
print('The last motorcycle I owned was a ' + lastOwned.title() + '.')
firstOwned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + firstOwned.title() + '.')

# ---------------------------------
# Using the remove() method
print('-' * 20)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Removing with variables
print('-' * 20)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
tooExpensive = 'ducati'
motorcycles.remove(tooExpensive)
print(motorcycles)
print('\nA ' + tooExpensive + ' is too expensive for me.')
