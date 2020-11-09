print("Give me twp numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input('\nFirst number: ')
    if firstNumber =='q':
        break
    secondNumber = input('Second number: ')
    if secondNumber == 'q':
        break
    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print('You cant divide by 0!')
    else:
        print(answer)