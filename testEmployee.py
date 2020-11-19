import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    '''Tests for the class Employee'''

    def setUp(self):
        '''Create an employee to test methods'''
        self.myEmployee = Employee('John', 'Doe', 60000)

    def testGiveDefaultRaise(self):
        '''Tests that the default raise is 5000'''
        self.myEmployee.giveRaise()
        self.assertEqual(self.myEmployee.salary, 65000)

    def testGiveCustomRaise(self):
        '''Tests that the custom raise wont break the class'''
        self.myEmployee.giveRaise(100)
        self.assertEqual(self.myEmployee.salary, 60100)

unittest.main()