# counting to 20
for number in range(1,21):
    print(number)

# counting to 1 mill
mill = []
for number in range(1,1000001):
    mill.append(number)
for num in mill:
    print(num)

# summing 1 mill
print(min(mill))
print(max(mill))
print(sum(mill))

# odd numbers
odd = list(range(1,21,2))
for number in odd:
    print(number)

# multiples of 3
threes = list(range(3,31,3))
for number in threes:
    print(number)

# cubing numbers 1-10
cubes = []
for number in range(1,11):
    cubes.append(number ** 3)
    print(cubes[-1])

# list comprehension
cubes = [number**3 for number in range(1,11)]
print(cubes)

# counting using a while loop instead of a for loop
num = 1
while num <= 5:
    print(num)
    num += 1

# counting odd numbers using continue
currentNum = 0
while currentNum < 10:
    currentNum += 1
    if currentNum % 2 == 0:
        continue
    
    print(currentNum)