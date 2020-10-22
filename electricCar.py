class Car():
    '''
    A simple attempt to represent a car.
    '''

    def __init__(self, make, model, year):
        '''Initialize attributes to discribe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def getDescriptiveName(self):
        '''Return a neatly formatted descriptive name.'''
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName.title()

    def readOdometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has ' + str(self.odometer) + ' miles on it.')
    def updateOdometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can\'t roll back an odometer!')

    def incrementOdometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer += miles



class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car,
        '''
        super().__init__(make, model, year)
        self.batterySize = 70

    def describeBattery(self):
        '''Print a statement describing the battery size.'''
        print('This car has a ' + str(self.batterySize) + '-kWh battery.')

myTesla = ElectricCar('tesla', 'model s', 2016)
print(myTesla.getDescriptiveName())
myTesla.describeBattery()