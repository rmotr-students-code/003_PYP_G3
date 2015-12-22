#-- Imports
import string

#-- Constants 
BOARD_SIZE = 10
EMPTY = " "
VERTICAL = 'V'
HORIZONTAL = 'H'
HIT = 'H'
MISS = 'M'
SHIP_SYMBOLS = ['A', 'S', '1', '2']

#-- Class declaration

class Board(object):

    def __init__(self):
        self.board = self.generate_board()

    def generate_board(self):
        """Generate an empty board"""
        board = {}
        for row in range(BOARD_SIZE):
           for col in range(BOARD_SIZE):
                board[(col, row)] = EMPTY
        return board
        
    def print_board(self, hide_ship = False):
        """Print the board on the console"""
        #Print col index
        print (" " * 1, end="")
        for i in range(BOARD_SIZE):
            print (" ", string.ascii_uppercase[i], end =" ")
        print ("")

        for row in range(BOARD_SIZE):
            #Print row index
            print (row + 1, " " * (1 - int((row + 1) / 10)), end="")

            for col in range(BOARD_SIZE):
                if hide_ship:
                    if self.board[(col, row)] in SHIP_SYMBOLS:
                        print (" ", end = " ")
                    else:
                        print(self.board[(col, row)], end = " ")
                else:
                    print(self.board[(col, row)], end = " ")
                if col < 9:
                    print ("|", end = " ")
            if row < 9:
                print ("\n", " " * 2, "---+" * 9, "---", sep="")
        print ("\n")

    def place_ship(self, ship, position, direction):
        """ 
        Take ship, starting position, direction as argument.
        If the ship can be placed update his position and direction and return True
        else return False
        """
        col = position[0]
        row = position[1]

        #Check if the ship will be out of bound
        if direction == HORIZONTAL:
            if col + ship.length > 9:
                return False
            else:
                #Check if two ships colide
                for i in range(ship.length):
                    if self.board[(col + i, row)] != EMPTY:
                        return False
                #Update value on the board
                for i in range(ship.length):
                    self.board[(col + i, row)] = ship.symbol
        elif direction == VERTICAL:
            if row + ship.length > 9:
                return False
            else:
                #Check if two ships colide
                for i in range(ship.length):
                    if self.board[(col, row + i)] != EMPTY:
                        return False
                    #Update value on the board
                for i in range(ship.length):
                    self.board[(col, row + i)] = ship.symbol
        else:
            raise ValueError("VERTICAL or HORIZONTAL expected as direction")

        ship.position = (col, row)
        ship.direction = direction
        
        return True

    def make_shot(self, position):
        """
        Make shot on position, return None if it miss, otherwise return the symbol of the
        ship which was hit 
        """
        if self.board[position] == HIT:
            raise ValueError("Position already shot")
        elif self.board[position] == EMPTY:
            self.board[position] = MISS
            return None
        else:
            symbol = self.board[position]
            self.board[position] = HIT
            return symbol
