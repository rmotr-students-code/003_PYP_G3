import board
import random
import ship

class Player(object):
    '''An interface class to represent a general player.'''
    
    def __init__(self, board, name):
        '''
        AH: The player probably only needs to keep track of 
        its own board and name
        '''
        self.board = board
        self.name = name

    
    def get_board(self):
        return self.board
    
    def toString(self):
        return self.name
    __str__ = toString
    
    
class HumanPlayer(Player):
    '''Subclass of Player to represent a human player'''
    
    def setup(self):
        '''
        The method for the setup/newgame phase,
        where he places all ships
        '''
        import ship
        SUBMARINE, AIRCRAFT, PATROL1, PATROL2 = ship.SUBMARINE, ship.AIRCRAFT, ship.PATROL1, ship.PATROL2
        BOAT_NAMES = ship.BOAT_NAMES
        BOAT_SIZES = ship.BOAT_SIZES
        
        print('Please select a ship to place:')
        ship_list = [SUBMARINE, AIRCRAFT, PATROL1, PATROL2]
        while len(ship_list) > 0:
            for i in ship_list:
                print(ship_list.index(i), BOAT_NAMES[i], 'Size: ', BOAT_SIZES[i])
            selection = int(input('Please select a ship to place: '))
            print(selection)
            if selection < len(ship_list):
                ship = ship_list.pop(selection)
                size = BOAT_SIZES[i]
                print('You selected', ship, 'Size:', size)
                place_successful = False
                while not place_successful:
                    self.board.printBoard("{}'s board".format(self.name))
                    orientation_input = input('Select orientation (h)orizontal or (v)ertical: ')
                    if str(orientation_input).lower() == 'h':
                        orientation = board.HORIZONTAL
                    else:
                        orientation = board.VERTICAL        
    
                    row = str(input('Enter the row for the highest point of your boat (eg: A): ')).upper()
                    col = str(input('Enter the column for the left most point of your boat (eg: 3): ')).upper()
                    if row in board.ROWS and col in board.COLS:
                        if self.board.placeShip(row, col, ship, orientation):
                            print('Ship placement successful')
                            place_successful = True
                        else:
                            print('Ship placement unsuccesful, try again')
            else:
                print('Invalid selection, try again!')
        print('Done!')
    
    def makeMove(self, otherBoard):
        '''
        Needs the other board since that's the one he's making
        moves at
        '''
        # While loop until done
        while True: 
            # Print the board
            otherBoard.printBoard("Other player's board", hideShips=True)
            
            # Ask for coordinates to shoot
            coord = input("Where do you want to shoot? Give a coordinate e.g. G4: ")
            if len(coord) < 2:
                continue
            row, col = coord[0], coord[1]
            
            # Attempt to shoot
            shotResult = otherBoard.placeShot(row, col)
            
            # Break out of loop if successful
            if shotResult == board.INVALID:
                print("Invalid shot. Try again.")
            else:
                print("Your shot was successful. You {}".format(shotResult.replace(board.HIT, "hit a ship!").replace(board.MISS, "missed!").replace(board.SUNK, "sunk a ship!")))
                break
    

class ComputerPlayer(Player):
    '''Subclass of Player to represent a computer player'''
    
    def __init__(self, the_board, name):
        super().__init__(the_board, name)
        self.possibleMoves = [row + col for row in board.ROWS for col in board.COLS]
            
    def setup(self):
        '''
        The method for the setup/newgame phase,
        where he places all ships
        '''
        # Loop until we have placed all ships
        shipsToPlace = 4
        while shipsToPlace > 0:
            # Generate a random coordinate
            row, col = random.choice(board.ROWS), random.choice(board.COLS)
            
            # Generate a random orientation
            orientation = random.choice([True, False])
            
            # Pick a random boat
            boat = random.choice(list(ship.BOAT_NAMES.keys()))
            
            # Attempt to place boat, reduce amount of boats to place if successful
            if self.board.placeShip(row, col, boat, orientation):
                shipsToPlace -= 1
    
    def makeMove(self, otherBoard, promptPlayer=False):
        '''
        Place random shots on the board (without repeats)
        
        otherBoard = the board the player will shoot at
        '''
        
        # Take a random move from the list of moves (self.possibleMoves)
        random.shuffle(self.possibleMoves)
        move = self.possibleMoves.pop()
        
        # Tell the player where the computer is shooting
        print("Computer shoots at {}.".format(move))
        if promptPlayer:
            otherBoard.printBoard("Your board")
            response = input("Was it a {} (hit), {} (miss) or {} (sunk)? ".format(board.HIT, board.MISS, board.SUNK)).upper()
            response = response.replace("HIT", board.HIT).replace("MISS", board.MISS).replace("SUNK", board.SUNK)
                
        # Place the shot
        shotResult = otherBoard.placeShot(move[0], move[1])
        
        # Check if the player was correct
        if promptPlayer:
            if not response == shotResult:
                print("You lie! It was a {}".format(shotResult))













# Possible testing code

