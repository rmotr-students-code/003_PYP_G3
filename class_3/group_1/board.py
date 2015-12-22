# Imports
from collections import OrderedDict
import ship

# Constants
HORIZONTAL = True
VERTICAL = False
EMPTY = " "
HIT = "X"
MISS = "O"
INVALID = "invalid"
SUNK = "S"
ROWS="ABCDEFGHIJ"
COLS="0123456789"


class Board(object):
    '''Class to represent the board'''
    
    def __generateBoard(rows=ROWS, cols=COLS):
        if len(rows) != len(cols):
            return None
        board = OrderedDict.fromkeys(rows)
        for row in rows:
            board[row] = OrderedDict.fromkeys(cols, EMPTY)

        return board
    
    def __init__(self, rows=ROWS, cols=COLS):
        self.board = Board.__generateBoard(rows, cols)
        self.ships = []
    
    def printBoard(self, ownerOfBoard="", hideShips=False):
        '''
        Prints the board
        '''
        print(ownerOfBoard)
        n = len(self.board.keys())
        horizontal_line = '\n  +-+' + '-+'*(n-2) + '-+'
        print(end='   ')
        for col in list(self.board.values())[0]:
            print(col, end=' ')
        print(horizontal_line)
        for row in self.board:
            print(row + ' |', end='')
            for col in self.board[row]:
                string = str(self.board[row][col])
                if hideShips and (string not in [HIT, MISS]):
                    string = EMPTY
                print(string, end='|')
            print(horizontal_line)

    def placeShip(self, row, col, ship_type, orientation):
        '''
        Takes row, col, orientation and ship type, detects if the ship
        can be placed there. Creates ship object and places it on the board or 
        fails if it can't be placed.
        Add the ship to a list in the board object.
        Returns True if successful, False if not
        '''
        import ship
        ship_size = ship.BOAT_SIZES[ship_type]
        
        # Make sure that that type of ship hasn't been placed yet
        for i in self.ships:
            if i.get_ship_type == ship_type:
                return False

        if orientation:
            ship_position = [row + chr(x) for x in range(ord(col), ord(col) + ship_size)]
        else:
            ship_position = [chr(x) + col for x in range(ord(row), ord(row) + ship_size)]
    
        # Make sure that the boat is in the borders of the board
        for i in ship_position:
            x, y = i[0], i[1]
            if x not in ROWS or y not in COLS:
                return False
            if self.board[x][y] != EMPTY:
                return False
                
        # Create ship object
        ship = ship.Ship(ship_type, ship_position)
        
        # Place that ship in each position of the board
        for pos in ship_position:
            x, y = pos[0], pos[1]
            self.board[x][y] = ship
            
        # Add the ship to the ship list
        self.ships.append(ship)
        
        return True
    
    def placeShot(self, row, col):
        '''
        return HIT/MISS/SUNK/INVALID, 
        
        '''
        row = row.upper()
        # Check if position is already shot at (HIT or MISS), return INVALID if so
        if self.board[row][col] in [HIT, MISS]:
            return INVALID
        
        # Else if empty return MISS
        if self.board[row][col] == EMPTY:
            self.board[row][col] = MISS
            return MISS
        
    
        # adjust in boats the corresponding boat and it's position to be HIT
        boat = self.board[row][col]
        boat.hit()
        self.board[row][col] = HIT
        
        # If boat is sunk, return SUNK
        if boat.hasSunk():
            return SUNK
        # Else return HIT
        else:
            return HIT
    
    def endGame(self):
        '''
        Returns True if the board has reached an end state, False otherwise
        '''
        # Check if all ships are sunk
        for boat in self.ships:
            if not boat.hasSunk():
                return False
        return True

# Possible testing code

