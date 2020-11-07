# Print the contents once by reading in the entire file
with open('learningPython.txt') as textObject:
    lines = textObject.read()
print('\n')
print(lines)

# Print the content once by looping over the file object
with open('learningPython.txt') as textObject:
    for line in textObject:
        print(line.strip())

# Print the content once by storing the lines in a list and 
# then working with them outside the with block
with open('learningPython.txt') as textObject:
    lines = textObject.readlines()
print('\n')

for line in lines:
    print(line.strip())

# Replacing the word "Python" with "C" and then printing
with open('learningPython.txt') as textObject:
    lines = textObject.read()
print('\n')
print(lines.replace('python', 'C'))