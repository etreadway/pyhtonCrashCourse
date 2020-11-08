fileName = 'programming.txt'

with open(fileName, 'w') as fo:
    fo.write('I love programming!\n')
    fo.write('I feel creative when I do it.\n')

# Using open() in a different way
# Also appending instead of writing to the file
fo = open(fileName, 'a')
fo.write('I want to try my hand at making games!\n')
fo.write('I want to use python to find meaning in large data sets!\n')
fo.write('I want to create apps that can run in a browser!\n')
fo.close()