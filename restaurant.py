class Restaurant():
    '''A class for discribing a restaurant. '''

    def __init__(self, name, foodType):
        '''Initialize name adn food type attributes.'''
        self.name = name
        self.foodType = foodType

    def discribeRestaurant(self):
        '''Describes the restaurant.'''
        print(self.name.title() + ' happily serves ' + self.foodType + ' food.')

    def openRestaurant(self):
        '''Tells customers that the restaurant is open'''
        print(self.name.title() + ' is open.')

molinas = Restaurant('molinas', 'Mexican')
whataburger = Restaurant('whataburger', 'fast')
colinas = Restaurant('colinas', 'mexican')


molinas.discribeRestaurant()
molinas.openRestaurant()

whataburger.discribeRestaurant()
whataburger.openRestaurant()

colinas.discribeRestaurant()
colinas.openRestaurant()