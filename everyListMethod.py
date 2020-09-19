# this is a list of vr head sets
vrHeadsets = ['vive', 'index', 'rift', 'quest', 'wmr']

# basic printing
print(vrHeadsets)

# printing individual elements from an index
print(vrHeadsets[0])

# printing with a title
print(vrHeadsets[0].title())

# printing the last thing on a list
print(vrHeadsets[-1])

# printing a sentence that uses an element with concatenation
print('I own a ' + vrHeadsets[0].title() +'.')

# modifying an element in a list
vrHeadsets[-1] = 'go'
print(vrHeadsets)

# appending an element to the list
vrHeadsets.append('wmr')
print(vrHeadsets)

# inserting an element into a list
vrHeadsets.insert(-1, 'pimax')
vrHeadsets.insert(-1, 'psvr')
print(vrHeadsets)

# deleting an element from the list
del vrHeadsets[-4]
print(vrHeadsets)

# poping an element from the list
budgetOption = vrHeadsets.pop()
print('I dont want ' + budgetOption + ' because they dont work too well')

# poping an element from a spacific spot on the list
unwanted = vrHeadsets.pop(-2)
print('I dont really want a ' + unwanted + ' because its waaaayyyy too expensive.')

# removing an item by its num
vrHeadsets.remove('psvr')
print(vrHeadsets)

# sorting a list permanently
vrHeadsets.sort()
print(vrHeadsets)
vrHeadsets.sort(reverse=True)
print(vrHeadsets)

# sorting temporarily
print(sorted(vrHeadsets))
print(vrHeadsets)

# reversing the current order
vrHeadsets.reverse()
print(vrHeadsets)

# finding/printing the length of a list
print(len(vrHeadsets))
