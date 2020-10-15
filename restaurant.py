class Restaurant():
    '''An class for discribing a restaurant. '''

    def __init__(self, name, foodType):
        '''Initialize name adnf food type attributes.'''
        self.name = name
        self.foodType = foodType

    def discribeRestaurant(self):
        '''Describes the restaurant.'''
        print(self.name.title() + ' happily serves ' + self.foodType + ' food.')

    def openRestaurant(self):
        '''Tells customers that the restaurant is open'''
        print(self.name.title() + ' is open.')

colinas = Restaurant('colinas', 'Mexican')

colinas.discribeRestaurant()
colinas.openRestaurant()