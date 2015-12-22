class Operation(object):

    @classmethod
    def operate(cls, x, y):
        raise NotImpementedError()

    @staticmethod
    def print_result(cls, x, y):
        print("The result of the operation is {}".format(cls.operate(x, y)))


class Sum(Operation):
    
    @classmethod
    def operate(cls, x, y):
        return x + y

Sum.print_result(2, 3)

"""
from random import randint

def random_number_generator(n=10000):
    while True:
        yield randint(0, n)


for idx, rndm in enumerate(random_number_generator()):
    print("{} - {}".format(idx, rndm))
    if idx == 4:
        break
"""
"""
class Operation(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operate(self):
        raise NotImpementedError()
        
    def to_string(self):
        return "The result of the operation is: {}".format(self.operate())


class Sum(Operation):
    NAME = 'Sum'
    def __operate(self):
        return self.x + self.y
        
    operate = __operate

class Subtract(Operation):
    def operate(self):
        return self.x - self.y


s = Sum(2, 3)
print(s.to_string())
"""

"""
class Ship(object):
    def __init__(self, initial_position, direction, size):
        self.initial_position = initial_position
        self.direction = direction
        self.size = size
        
    def mark_shot(self, position):
        if ...:
            self.sunk = True

class Aircraft(Ship):
    def __init__(self, initial_position, direction):
        super(Aircraft, self).__init__(initial_position, direction, size=5)

aircraft1 = Aircraft('A1', 'horizontal')

class Submarine(Ship):
    def __init__(self, initial_position, direction):
        self.initial_position = initial_position
        self.direction = direction
        self.size = 3


class Board(object):
    
    def __init__(self, no_columns=10, no_rows=10):
        self.no_columns = no_columns
        self.no_rows = no_rows
        self.ships = []

    def place_ship(self, ship):
        self.ships.append(ship)

    def take_shot(self, position):
        ship = self.ship_in_position(position)
        if ship:
            ship.mark_shot(position)


aircraft1 = Aircraft('A1', 'horizontal')
submarine = Submarine('C5', 'vertical')

board = Board()
board.place_ship(aircraft)
board.place_ship(submarine)
board.take_shot(position)
"""


"""

class Car(object):
    def __init__(self, model, owners_name, used=False, **kwargs):
       self.model = model
       self.owners_name = owners_name
       self.used = used

    def print_model(self):
        print("My model is: {}".format(self.model))


c1 = Car(model='S', owners_name="Tom")
c1.print_model()

c2 = Car(model='T', owners_name="Mary")
c2.print_model()
"""