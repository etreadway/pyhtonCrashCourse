import unittest
from nameFunction import getFormattedName

class NamesTestCase(unittest.TestCase):
    '''Tests for "nameFunction.py".'''

    def testFirstLastName(self):
        '''Do names like "Janis Joplin" work?'''
        formattedName = getFormattedName('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def testFirstLastMiddleName(self):
        '''Do names like "Wolfgang Amadeus Mozart" work?'''
        formattedName = getFormattedName('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formattedName, 'Wolfgang Amadeus Mozart')

unittest.main()