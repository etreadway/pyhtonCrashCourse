# copying a list to another list
myFoods = ['pizza', 'falafel', 'carrot cake']
friendFoods = myFoods[:]

# # this doesn't work
# friendFoods = myFoods


myFoods.append('cannoli')
friendFoods.append('ice cream')

# printing my favorite foods
print('My favorite foods are:')
# print(myFoods)
for food in myFoods:
    print(food)

# printing my friends favorite foods
print('\nMy friends favorite foods are:')
# print(friendFoods)
for food in friendFoods:
    print(food)