class Employee():
    '''A simple class to take and store the name and salary of an employee'''

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def printInfo(self):
        print('First Name: ' + self.firstName)
        print('Last Name: ' + self.lastName)
        print('Salary: $' + str(self.salary))

    def giveRaise(self, salaryIncrease=5000):
        self.salary += salaryIncrease

test = Employee('john', 'doe', 10000)

