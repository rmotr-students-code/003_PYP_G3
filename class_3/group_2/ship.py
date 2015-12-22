#-- Imports

#-- Constants
SUBMARINE = 'SUBMARINE'
AIRCRAFT = 'AIRCRAFT'
PATROL1 = 'PATROL1'
PATROL2 = 'PATROL2'
SHIPS = [SUBMARINE, AIRCRAFT, PATROL1, PATROL2]
SHIP_SIZES = {SUBMARINE : 3, AIRCRAFT : 5, PATROL1 : 2, PATROL2 : 2}
SHIP_SYMBOLS = {SUBMARINE : 'S', AIRCRAFT : 'A', PATROL1 : '1', PATROL2 : '2'}

#-- Class

class Ship(object):

	def __init__(self, ship_type, position = None, direction = None):
		self.ship_type = ship_type
		self.position = position
		self.direction = direction
		self.symbol = SHIP_SYMBOLS[ship_type]
		self.length = SHIP_SIZES[ship_type]
		self.health = SHIP_SIZES[ship_type]

	def hit(self):
		if self.health > 0:
			self.health -= 1

	def is_sunk(self):
		return self.health == 0
