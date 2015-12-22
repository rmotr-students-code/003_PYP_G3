# Imports


# Constants

SUBMARINE = 0
AIRCRAFT = 1
PATROL1 = 2
PATROL2 = 3
BOAT_SIZES = {SUBMARINE : 3, AIRCRAFT : 5, PATROL1 : 2, PATROL2 : 2}
BOAT_NAMES = {SUBMARINE : "SUBMARINE", AIRCRAFT : "AIRCRAFT", PATROL1 : "PATROL1", PATROL2 : "PATROL2"}


class Ship(object):
    '''Class to represent ships on the board'''
    
    def __init__(self, ship_type, positions):
        '''

        '''
        self.ship_type = ship_type
        self.positions = positions
        self.health = BOAT_SIZES[ship_type]
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
    
    def hasSunk(self):
        '''
        Returns True if the ship has sunk, False otherwise
        '''
        return self.health == 0
    
    def get_ship_type(self):
        return self.ship_type
    
    def toString(self):
        return "Ship type: {} \t Positions: {} \t Health remaining: {}".format(self.ship_type, self.positions, self.health)
    
    def __str__(self):
        return str(self.ship_type)
    




# Possible testing code

