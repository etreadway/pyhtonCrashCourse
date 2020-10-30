'''A class that can be used to represent a car.'''

class Car():
    '''A simple attempt tp represent a car.'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self. year = year
        self.odometerReading = 0
    
    def getDescriptiveName(self):
        '''Return a neatly formated descriptive name.'''
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName.title()

    def readOdometer(self):
        '''Print a statement shoeing the car's mileage.'''
        print('This car has ' + str(self.odometerReading) + ' miles on it.')
    
    def updateOdometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print('You can\'t roll back an odometer!')
    
    def incrementOdometer(self, miles):
        '''Add the given anount to the odometer reading'''
        self.odometerReading += miles