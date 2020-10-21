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

myNewCar = Car('tesla', 'cyber truck', 2021)
print(myNewCar.getDescriptiveName())

# # Modifying an attributes value directly
# myNewCar.odometer = 42

# Modifying an attributes value through a method
myNewCar.updateOdometer(42)
myNewCar.readOdometer()

myUsedCar = Car('subaru', 'outback', 2013)
print(myUsedCar.getDescriptiveName())

myUsedCar.updateOdometer(23500)
myUsedCar.readOdometer()
myUsedCar.incrementOdometer(100)
myUsedCar.readOdometer()