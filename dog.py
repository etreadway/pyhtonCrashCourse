class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        '''Initalize name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command.'''
        print(self.name.title() + ' is now sitting.')

    def rollOver(self):
        '''Simulate a dog rolling over in response to a command.'''
        print(self.name.title() + ' rolled over!')

bug = Dog('doodle bug', 5)
burrow = Dog('burrow', 3)

print('My dog\'s name is ' + bug.name.title() + '!')
print('My dog is ' + str(bug.age) + ' years old,')

bug.sit()
bug.rollOver()

print('\n')
print('My dog\'s name is ' + burrow.name.title() + '!')
print('My dog is ' + str(burrow.age) + ' years old,')

burrow.sit()
burrow.rollOver()