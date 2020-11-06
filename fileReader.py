fileName = 'piDigits.txt'

with open(fileName) as fileObject:
    lines = fileObject.readlines()

for line in lines:
    print(line.rstrip())