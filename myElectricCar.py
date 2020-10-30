from car2 import ElectricCar

myTesla = ElectricCar('tesla', 'cyber truck', 2021)

print(myTesla.getDescriptiveName())
myTesla.battery.describeBattery()
myTesla.battery.getRange()