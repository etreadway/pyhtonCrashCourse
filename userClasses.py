class User():
    '''
    A class for describing a user.
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

class Admin(User):
    '''Represents aspects of a user that are specific to the Admin.'''
    def __init__(self, firstName, lastName, age, gender):
        '''
        Initialize aspects of the parent class.
        Also initialize aspects of the child class.
        '''
        super().__init__(firstName, lastName, age, gender)
        self.privileges = Privileges()

class Privileges():
    '''An attempt to containerize the privilege attribute'''

    def __init__(self):
        self.privileges = ['add post',
                           'delete post',
                           'edit post',
                           'ban user',
                           'make announcement',
                           ]


    def showPrivileges(self):
        print('\nYour admin privileges are:')
        for privilege in self.privileges:
            print(privilege)