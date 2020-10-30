'''Importing multiple classes from the module'''
# from car2 import Car, ElectricCar
# myCorolla = Car('toyota', 'corolla', 2012)
# print(myCorolla.getDescriptiveName())

# myTesla = ElectricCar('tesla', 'cyber truck', 2021)
# print(myTesla.getDescriptiveName())

'''Importing the entire module (Note the car2.Car and car2.ElectricCar)'''
# import car2

# myCorolla = car2.Car('toyota', 'corolla', 2012)
# print(myCorolla.getDescriptiveName())

# myTesla = car2.ElectricCar('tesla', 'cyber truck', 2021)
# print(myTesla.getDescriptiveName())

'''importing all classes from module (Note that I am importing a "*")'''
from car2 import *

myCorolla = Car('toyota', 'corolla', 2012)
print(myCorolla.getDescriptiveName())

myTesla = ElectricCar('tesla', 'cyber truck', 2021)
print(myTesla.getDescriptiveName())