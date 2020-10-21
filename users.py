class User():
    '''
    A class for discribing a user.
    '''

    def __init__(self, firstName, lastName, age, gender):
        """
        Initialize basic info about the user.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender
        self.loginAttempts = 0
    
    def discribeUser(self):
        """
        Prints a summary of the user information.
        """
        print('\n')
        print('User Summary')
        print('*' * 12)
        print('First: ' + self.firstName.title())
        print('Last: ' + self.lastName.title())
        print('Age: ' + str(self.age))
        print('Gender: ' + self.gender.title())
    
    def greetUser(self):
        print('\n')
        firstLast = self.firstName.title() + ' ' + self.lastName.title()

        # preforming a gender check
        genderTerm = ''
        if self.gender.lower() == 'f':
            genderTerm = 'beautiful'
        elif self.gender.lower() == 'm':
            genderTerm = 'handsome'
        else:
            genderTerm = 'stunning'
        
        print('Well if it isn\'t the ' + genderTerm + ' ' + firstLast + '!')
        print('Looking great for ' + str(self.age) + '.')

    def incrementLoginAttempt(self):
        '''A method to keep track of login attempts.'''
        self.loginAttempts += 1

    def resetLoginAttempt(self):
        '''A method to reset the number of login attempts.'''
        self.loginAttempts = 0



theo = User('theo','logen', 52, 'm')
holly = User('holly', 'wood', 67, 'f')

theo.discribeUser()
theo.greetUser()

holly.discribeUser()
holly.greetUser()

print('\n')
theo.incrementLoginAttempt()
theo.incrementLoginAttempt()
theo.incrementLoginAttempt()
theo.incrementLoginAttempt()
print(theo.loginAttempts)
theo.resetLoginAttempt()
print(theo.loginAttempts)