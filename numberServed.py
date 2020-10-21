class Restaurant():
    '''A class for discribing a restaurant. '''

    def __init__(self, name, foodType):
        '''Initialize name adn food type attributes.'''
        self.name = name
        self.foodType = foodType
        self.numberServed = 0

    def discribeRestaurant(self):
        '''Describes the restaurant.'''
        print(self.name.title() + ' happily serves ' + self.foodType + ' food.')

    def openRestaurant(self):
        '''Tells customers that the restaurant is open.'''
        print(self.name.title() + ' is open.')

    def setNumberServed(self, customers):
        '''Sets the number of served customers.'''
        self.numberServed = customers
    def incrementNumberServed(self, increase):
        self.numberServed += increase


testRest = Restaurant('good burger', 'american')
print(str(testRest.numberServed))
testRest.numberServed = 19
print(str(testRest.numberServed))
testRest.setNumberServed(42)
print(str(testRest.numberServed))
testRest.incrementNumberServed(378)
print(str(testRest.numberServed))