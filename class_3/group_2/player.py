#-- Imports
import random
import string

#-- Constants
VERTICAL = 'v'
HORIZONTAL = 'h'
HIT = 'H'
MISS = 'M'

class Player(object):

    def __init__(self, board, name):
        self.board = board
        self.name = name

class HumanPlayer(Player):

    def place_ship(self, ships):
        for ship in ships:
            while self.board.place_ship(ship, *self.ask_user_ship_position(ship)) == False:
                pass
        self.board.print_board()
    
    def ask_user_ship_position(self, ship):
        """Ask the user for a position and a direction, return a valid position and direction"""
        print (chr(27) + "[2J")
        print ("==== Place your {}, length : {} ====\n".format(ship.ship_type, ship.length))
        self.board.print_board()
        position = input("Please enter the starting position of your ship :".format(ship.ship_type))
        col = position[0].upper()
        row = int(position[1:]) - 1
        if col not in string.ascii_uppercase[:10] or row not in range(10):
            print ("You can only enter a letter between A - J followed by a number between 1 - 10")
        else:
            position = (ord(col) - 65, row)
            direction = None
            while direction != 'H' and direction != 'V':
                direction = input("Please enter the orientation of your ship (H for Horizontal or V for Vertical) : ")
                if direction != 'H' and direction != 'V':
                    print ("Please enter a valid orientation")
                else:
                    return position, direction
                    
    def make_move(self, ennemy_board):
        """Make a move and print the result"""
        position = self.ask_user_move()
        outcome = ennemy_board.make_shot(position) 
        if outcome == HIT:
            print("You hit a ship !")
        else outcome == MISS:
            print("You missed !")
        return outcome
    
    def ask_user_move(self):
        """Ask the user for his move, return a valid position"""
        print (chr(27) + "[2J")
        print ("==== Make your move ====\n".format(ship.ship_type, ship.length))
        self.board.print_board()
        position = input("Where do you want to shoot ? :")
        col = position[0].upper()
        row = int(position[1:]) - 1
        if col not in string.ascii_uppercase[:10] or row not in range(10):
            print ("You can only enter a letter between A - J followed by a number between 1 - 10")
        else:
            return (ord(col) - 65, row)

class ComputerPlayer(Player):

    def __init__(self, board, name):
        super().__init__(board, name)
        self.possible_moves = list(self.board.board.keys())

    def place_ship(self, ships):
        """ Take a list of ship as argument and place them on the board"""
        available_positions = list(self.board.board.keys())
        availbale_directions = [HORIZONTAL, VERTICAL]
        random.shuffle(available_positions)

        for ship in ships:
            while self.board.place_ship(ship, available_positions.pop(), random.choice(availbale_directions)) == False:
                pass

    def make_move(self, ennemy_board):
        """ Make a random shot on the ennemy board """
        random.shuffle(self.possible_moves)
        return ennemy_board.make_shot(self.possible_moves.pop())



