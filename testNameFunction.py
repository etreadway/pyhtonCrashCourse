import unittest
from nameFunction import getFormattedName

class NamesTestCase(unittest.TestCase):
    '''Tests for "nameFunction.py".'''

    def testFirstLastName(self):
        '''Do names like "Janis Joplin" work?'''
        formattedName = getFormattedName('janis', 'joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

unittest.main()