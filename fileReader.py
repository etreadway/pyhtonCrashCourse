fileName = 'piDigits.txt'

with open(fileName) as fileObject:
    for line in fileObject:
        print(line.rstrip())