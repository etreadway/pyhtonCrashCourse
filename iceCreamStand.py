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

class IceCreamStand(Restaurant):
    '''
    Represents aspects of a restaurant that are specific to an ice cream stand.
    '''
    def __init__(self, name, foodType):
        '''
        Initialize aspects of the parent class.
        Then initialize aspects of the child class.
        '''
        super().__init__(name, foodType)
        self.flavors = ['vanilla',
                        'chocolate',
                        'strawberry',
                        'birthday cake',
                        'lavender',
                        ]

    def displayFlavors(self):
        print('\nTODAY\'S FLAVORS')
        print('-' * len('\nTODAY\'S FLAVORS'))
        for element in self.flavors:
            print(element)

iceCream = IceCreamStand('h and e ice cream', 'ice cream')

iceCream.discribeRestaurant()
iceCream.openRestaurant()
iceCream.displayFlavors()