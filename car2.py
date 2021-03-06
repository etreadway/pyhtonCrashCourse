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

class Battery():
    '''A simple attempt to model a battery.'''

    def __init__(self, batterySize=70):
        '''Initialize the battery's attributes.'''
        self.batterySize = batterySize

    def describeBattery(self):
        '''Print a statement describing the battery sizy.'''
        print('This car has a ' + str(self.batterySize) + '-kWh battery.')

    def getRange(self):
        '''Print a statement about the range this battery provides.'''
        if self.batterySize == 70:
            carRange = 240
        elif self.batterySize == 85:
            carRange = 270

        message = 'This car can go approximately ' + str(carRange)
        message += ' miles on a full charge.'
        print(message)

    def upgradeBattery(self):
        '''A method for upgrading the batery.'''
        if self.batterySize <= 85:
            self.batterySize = 85
            print('Your battery has been upgraded!')
        elif self.batterySize == 85:
            print('You have already been upgraded.')
        elif self.batterySize >= 85:
            print('This would be a downgrade.')


class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car,
        '''
        super().__init__(make, model, year)
        self.battery = Battery()
