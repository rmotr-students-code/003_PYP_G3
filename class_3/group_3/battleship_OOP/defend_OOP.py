"""Controls the defence workflow of the game."""

import random
from classes import *

def defend_phase(ships, grid):
    """Controls the attack sequence of the computer until it sinks all the user's ships. 
    
    Args:   
        The board of play.
        
    Returns:
        None
    """
    positions_attacked = [] #Tuple of each position chosen.
    result_of_attack = [] #Binary result of attack: 1 for a hit and 0 for a miss.
    rounds = 0
    flag = True
    
    while flag==True:
        #AI picks a random spot to attack.
        guess = (random.choice([i for i in range(0,grid.size)]), random.choice([i for i in range(0,grid.size)]))
        while guess in positions_attacked:
            guess = (random.choice([i for i in range(0,grid.size)]), random.choice([i for i in range(0,grid.size)]))
        positions_attacked.append(guess)
        
        print('\n')
        grid.print_board()
        print('\n')
        
        print('I guess '+str(guess)+'. Did I hit, miss or sink a ship? \n')
        user_answer = raw_input("Type 'h' (hit), 'm' (miss) or 's' (sink): ").lower() #need to add sink option
        while user_answer not in ['h','s','m']:
            user_answer = raw_input("Please type 'h' (hit), 'm' (miss) or 's' (sink): ")
        print('\n')
            
        if grid.board[guess[0]][guess[1]] == '#':
            if user_answer == 'm':
                print("You're lying."), #Didn't bother with other variations of lying. Not worth the time. 
            print("Hit.\n")
            result_of_attack.append(1)
            grid.board[guess[0]][guess[1]] = 'X'
            check_sink(guess[0],guess[1],ships,grid)
        else:
            print('Missed.\n')
            result_of_attack.append(0)
        
        rounds+=1
        list_check = [pos for col in grid.board for pos in col]
        if '#' not in list_check:
            print('The computer has sunken all your ships.')
            flag = False
    
    print('\nSTATISTICS: The computer took '+str(rounds)+' rounds to sink all your ships.')        

def defend():
    """Controls the setup of the game for the user's defence. 
    
    Args:   
        None
        
    Returns:
        None
    """
    grid = Grid(10,10)
    aircraft = Aircraft()
    submarine = Submarine()
    patrol_boat1 = PatrolBoat()
    patrol_boat2 = PatrolBoat()
    ships = [aircraft,submarine,patrol_boat1,patrol_boat2]
    print('Please places your ships. \n')
    place_ships(grid,ships)
    defend_phase(ships, grid)
   
def place_ships(grid, ships): 
    """Sets the user's ships on the board. 
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    #Assigns an orientation and position to every ship
    for ship in ships: 
        orientation = raw_input("Do you want the orientation of the "+ship.name+" to be vertical or horizontal? Enter 'h' for horizontal and 'v' for vertical: ")
        while orientation not in ('h','v'):
            orientation = raw_input("Please enter either 'h' for horizontal and 'v' for vertical: ")
            
        x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
        while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
        x = int(x)
            
        y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
        while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
        y = int(y)
        position = (x,y)
        position = check_position(grid, ship, position, orientation)
        ship.orientation = orientation
        
        #Fills the spaces occupied by each ship with an 'X' and logs these spaces for each ship as its position.
        if ship.orientation == 'h':
            for y in range(position[1],position[1]+ship.size):
                grid.board[position[0]][y] = '#'
                ship.location.append((position[0],y))
        elif ship.orientation== 'v':
            for x in range(position[0],position[0]+ship.size):
                grid.board[x][position[1]] = '#'
                ship.location.append((x,position[1]))

        grid.print_board()
        print('\n')
        
def check_position(grid, ship, position, orientation):
    """Checks to make sure that each user ship is on the board and doesn't collide with another. 
    
    Args:   
        The board of play, a ship, its orientation, and the proposed position of the ship.
        
    Returns:
        A possibly new position.
    """
    #Corrects positioning off the field of play.
    if orientation == 'h':
        while position[1]+ship.size > grid.size - 1:
            print('The ship is off board. Enter new positions')
            grid.print_board()
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            y = int(y)
            position = (x,y)
    elif orientation == 'v':
        while position[0] + ship.size > grid.size - 1:
            print('The ship is off board. Enter new positions')
            grid.print_board()
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            y = int(y)
            position = (x,y)
            
    #Corrects collison with another ship.      
    if orientation == 'h':
        while '#' in [grid.board[position[0]][y] for y in range(position[1],position[1]+ship.size)]:
            print('The ship collides with another. Enter new positions')
            grid.print_board()
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            y = int(y)
            position = (x,y)
    elif orientation == 'v':
       while '#' in [grid.board[x][position[1]] for x in range(position[0],position[0]+ship.size)]:
            print('The ship collides with another. Enter new positions')
            grid.print_board()
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship.name+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship.name+'? ')
            y = int(y)
            position = (x,y)
            
    return position

def check_sink(x,y,ships,grid):
    """Checks to see if a ship has been sunk.
    
    Args:   
        The x and y position of the hit, the grid, and the computer's ships.
        
    Returns:
        Whether or not a ship has sunk.
    """
    hit = (x,y)
    for ship in ships:
        if hit in ship.location:
            hit_ship = ship
            
    sunk_check = set([grid.board[i[0]][i[1]] for i in hit_ship.location])
    
    if sunk_check == set(['X']):
        print("The computer sank your {}".format(hit_ship.name))
        print('\n')   
    
    