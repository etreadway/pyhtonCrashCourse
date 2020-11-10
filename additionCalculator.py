# taking user input for two numbers and adding them together

print('Give me two numbers and I will add them together.')
while True:
    try:
        firstNum = int(input('What is the first number? '))
        secondNum = int(input('What is the second number? '))
    except ValueError:
        print('That is not a number.')
    else:
        answer = firstNum + secondNum
        print(answer)

    check = input('Would you like to add two more numbers? (Y/n) ')
    if check.lower() == 'n':
        break