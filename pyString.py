filename = 'pi_million_digits.txt'

with open(filename) as fileObject:
    lines = fileObject.readlines()

piString = ''
for line in lines:
    piString += line.strip()

print(piString[:52] + '...')
print(len(piString))