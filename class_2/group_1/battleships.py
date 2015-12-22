"""
Group exercise

Build a battleship game. It has to work in the console. You don't need any external libraries, you can make it work just using plain python. 
You'd play against the console. The game will have 2 play modes: attack or defence.

Defend mode

In this mode you place the ships and receive attacks from the computer; you’ll have to inform if the attack was successful or not.

When the game starts the computer will give you information about the grid (10x10) and tell you what ships you have available. For example:

    1 submarine (size 3)
    1 Aircraft (size 5)
    2 Patrol boats (size 2)

Then you’ll be able to position them in the grid, indicating the first position and if they should be placed horizontally or vertically. Example:

    Place the submarine on C3 vertically
    Place the aircraft on A9 horizontally

At this point the computer must do some checks; namely:

    If the ship fits; it’s not out of bounds. For example, placing an Aircraft on the position H9 horizontally would make it go out of bounds
    If two ships collide. For example. Placing the submarine on C3 vertically and the aircraft on B1 horizontally.

After the setup is done (ship positioning) you’ll start receiving random attacks from the computer; 1 at a time. 
After the computer attacks it’ll ask for an answer from you (either miss, hit or sunk). You’ll inform the computer (seeing the grid on screen). 
If you cheat, the computer should know.

Of course the computer would never fire two shots at the same position; and would realize when it sunk all the ships.

Extra: Once the computer identifies it has hit a ship the attacks could stop being random and focus on sinking that particular ship it hit.

Attack mode

In this mode the computer position the ships and you’ll have to sink all of them. 
The computer will position the ships randomly. After it’s done it’ll start asking for your shots. 
Once you fire your shot it’ll inform you if you missed, hit or sunk a ship. Once all the ships are sunk the game finishes and it’ll provide statistics about it.
"""

from collections import OrderedDict
import random

#Constants
SUBMARINE = 0
AIRCRAFT = 1
PATROL1 = 2
PATROL2 = 3
BOAT_SIZES = {SUBMARINE : 3, AIRCRAFT : 5, PATROL1 : 2, PATROL2 : 2}
BOAT_NAMES = {SUBMARINE : "SUBMARINE", AIRCRAFT : "AIRCRAFT", PATROL1 : "PATROL1", PATROL2 : "PATROL2"}
EMPTY = " "
HIT = "X"
MISS = "O"
INVALID = "invalid"
SUNK = "S"
HORIZONTAL = True
VERTICAL = False
ROWS="ABCDEFGHIJ"
COLS="0123456789"

#Globals
playerBoard = {}
playerBoats = {}
computerBoard = {}
computerBoats = {}
computerMoves = {}


def mainGameLoop(playerBoard, playerBoats, computerBoard, computerBoats, mode="standard"):
    mode = mode.lower()
    if mode not in ["standard", "attack", "defend"]:
        print('You have chosen an invalid mode. Mode is defaulted to "standard"')
        mode = "standard"
    
    while True:
        # Player turn
        if mode == "standard" or mode == "attack":
            # Ask player for move
            playerMove(computerBoard, computerBoats)
            
            # Check if the game has ended, break if so
            if isEnd(computerBoard, computerBoats):
                print("You win!")
                break
        
        # Computer turn
        if mode == "standard" or mode == "defend":
            # Ask for other player move (computer)
            computerMove(playerBoard, playerBoats, mode == "defend")
            
            # Check if the game has ended, break if so
            if isEnd(playerBoard, playerBoats):
                print("Computer wins!")
                break
        print("\nEnd of round\n" + "-"*30 + "\n")

def playerMove(board, boats):
    '''
    Prompt player for shots
    
    board = the board the player will shoot at
    boats = boats to corresponding board
    '''
    
    # While loop until done
    while True: 
        # Print the board
        printBoard(board, "Other player's board", hideShips=True)
        
        # Ask for coordinates to shoot
        coord = input("Where do you want to shoot? Give a coordinate e.g. G4: ")
        row, col = coord[0], coord[1]
        
        # Attempt to shoot
        shotResult = placeShot(board, boats, row, col)
        
        # Break out of loop if successful
        if shotResult == INVALID:
            print("Invalid shot. Try again.")
        else:
            print("Your shot was successful. You {}".format(shotResult.replace(HIT, "hit a ship!").replace(MISS, "missed!").replace(SUNK, "sunk a ship!")))
            break

def computerMove(board, boats, promptPlayer=False):
    '''
    Place random shots on the board (without repeats)
    
    board = the board the player will shoot at
    boats = boats to corresponding board
    '''
    global computerMoves
    # Take a random move from the list of moves (computerMoves)
    random.shuffle(computerMoves)
    move = computerMoves.pop()
    
    # Tell the player where the computer is shooting
    print("Computer shoots at {}.".format(move))
    if promptPlayer:
        printBoard(board, "Your board")
        response = input("Was it a {} (hit), {} (miss) or {} (sunk)? ".format(move, HIT, MISS, SUNK)).upper()
        response = response.replace("HIT", HIT).replace("MISS", MISS).replace("SUNK", SUNK)
            
    # Place the shot
    shotResult = placeShot(board, boats, move[0], move[1])
    
    # Check if the player was correct
    if promptPlayer:
        if not response == shotResult:
            print("You lie! It was a {}".format(shotResult))
        
    

def placeShot(board, boats, row, col):
    '''
    Test if shot is hit/miss or ship sunk
    
    board = the board to shoot at
    boats = boats to corresponding board
    row = A-J
    col = 0-9
    
    returns HIT, MISS, INVALID or SUNK
    '''
    
    # Check if position is already shot at (HIT or MISS), return INVALID if so
    if board[row][col] in [HIT, MISS]:
        return INVALID
    
    # Else if empty return MISS
    if board[row][col] == EMPTY:
        board[row][col] = MISS
        return MISS
    

    # adjust in boats the corresponding boat and it's position to be HIT
    boat = board[row][col]
    index = boats[boat].index(row + col)
    boats[boat][index] = HIT
    board[row][col] = HIT
    # If boat is sunk, return SUNK
    if boats[boat].count(HIT) == BOAT_SIZES[boat]:
        return SUNK
    # Else return HIT
    else:
        return HIT


def isEnd(board, boats):
    '''
    Test if game has finished (test if all ships are sunk)
    
    board = the board to check end condition
    boats = boats to corresponding board
    
    returns true or false
    '''
    
    # Simply check if all boats are sunk
    for boat in boats:
        for cell in boats[boat]:
            if not cell == HIT:
                return False
    return True

def newGame(mode="standard"):
    '''
    Generate empty boards
    Run setup for players
    '''
    print('Welcome to Battleship!')
    global playerBoard, playerBoats, computerBoard, computerBoats, computerMoves

    if mode == "standard" or mode == "defend":
        playerBoard = generateBoard()
        playerBoats = OrderedDict.fromkeys(BOAT_NAMES, [])
        playerSetup(playerBoard, playerBoats)
        computerMoves = [row + col for row in ROWS for col in COLS]
    
    if mode == "standard" or mode == "attack":
        computerBoard = generateBoard()
        computerBoats = OrderedDict.fromkeys(BOAT_NAMES, [])
        computerSetup(computerBoard, computerBoats)
    

def playerSetup(board, boats):
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
                printBoard(board, 'Player')
                orientation_input = input('Select orientation (h)orizontal or (v)ertical: ')
                if str(orientation_input).lower() == 'h':
                    orientation = HORIZONTAL
                else:
                    orientation = VERTICAL        

                row = str(input('Enter the row for the highest point of your boat (eg: A): ')).upper()
                col = str(input('Enter the column for the left most point of your boat (eg: 3): ')).upper()
                if row in ROWS and col in COLS:
                    if placeShip(board, boats, row, col, ship, orientation):
                        print('Ship placement successful')
                        place_successful = True
                    else:
                        print('Ship placement unsuccesful, try again')
        else:
            print('Invalid selection, try again!')
    print('Done!')

def computerSetup(board, boats, shipsToPlace=4):
    
    # Loop until we have placed all ships
    while shipsToPlace > 0:
        # Generate a random coordinate
        row, col = random.choice(ROWS), random.choice(COLS)
        
        # Generate a random orientation
        orientation = random.choice([True, False])
        
        # Pick a random boat
        boat = random.choice(list(BOAT_NAMES.keys()))
        
        # Attempt to place boat, reduce amount of boats to place if successful
        if placeShip(board, boats, row, col, boat, orientation):
            shipsToPlace -= 1
        

    
def placeShip(board, boats, row, col, boat, orientation):
    '''
    Test if the ship can be placed on the board
    ''' 
    boat_size = BOAT_SIZES[boat]

    # Check if the boat is already placed
    if boats[boat]:
        return False

    if orientation:
        boat_position = [row + chr(x) for x in range(ord(col), ord(col) + boat_size)]
    else:
        boat_position = [chr(x) + col for x in range(ord(row), ord(row) + boat_size)]

    # Make sure that the boat is in the board
    for i in boat_position:
        x, y = i[0], i[1]
        if x not in ROWS or y not in COLS:
            return False
        if board[x][y] != EMPTY:
            return False
           
    # Place boat on board
    for i in boat_position:
        x, y = i[0], i[1]
        board[x][y] = boat
    
    # Place boat in dict
    boats[boat] = boat_position
    
    return True


def printBoard(board, ownerOfBoard="", hideShips=False):
    print(ownerOfBoard)
    n = len(board.keys())
    horizontal_line = '\n  +-+' + '-+'*(n-2) + '-+'
    print(end='   ')
    for col in list(board.values())[0]:
        print(col, end=' ')
    print(horizontal_line)
    for row in board:
        print(row + ' |', end='')
        for col in board[row]:
            string = str(board[row][col])
            if hideShips and (string not in [HIT, MISS]):
                string = EMPTY
            print(string, end='|')
        print(horizontal_line)


def generateBoard(rows=ROWS, cols=COLS):
    if len(rows) != len(cols):
        return None
    board = OrderedDict.fromkeys(rows)
    for row in rows:
        board[row] = OrderedDict.fromkeys(cols, " ")
 
    return board

mode = input('What mode do you want to play ("standard", "attack", "defend")? ')
newGame(mode)
mainGameLoop(playerBoard, playerBoats, computerBoard, computerBoats, mode)