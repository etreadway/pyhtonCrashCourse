# intro to tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# with a for loop
print('with a for loop')
for dimension in dimensions:
    print(dimension)

# writing over a tuple
dimension = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)