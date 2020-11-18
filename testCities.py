import unittest
from cityCountry import cityCountry

class CityTestCase(unittest.TestCase):
    '''Tests for cityCountry.py'''

    def testCityCountry(self):
        '''Do places like Santiago, Chile work?'''
        formattedlocation = cityCountry('santiago', 'chile')
        self.assertEqual(formattedlocation, 'Santiago, Chile')
    def testPopulationIncluded(self):
        formattedlocation = cityCountry('santiago', 'chile', 5600000)
        self.assertEqual(formattedlocation, 'Santiago, Chile, 5600000')
unittest.main()