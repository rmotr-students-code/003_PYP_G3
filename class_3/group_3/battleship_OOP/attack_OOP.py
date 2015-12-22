from classes import *
import random

def attack():
    """Controls attack phase.
    
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
    print('Please wait while the computer places its ships. \n')
    place_ships(grid,ships)
    attack_phase(ships, grid)
    
def place_ships(grid,ships): 
    """Sets the computer's ships on the board.
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    #Assigns an orientation and position to every ship.
    for ship in ships: 
        orientation = random.choice(['h','v'])
        position = (random.choice([i for i in range(0,grid.size)]),random.choice([i for i in range(0,grid.size)]))
        position = check_position(grid, ship, position, orientation)
        ship.orientation = orientation
        
        #Fills the spaces occupied by each ship with an 'X'.
        if ship.orientation == 'h':
            for y in range(position[1],position[1]+ship.size):
                grid.board[position[0]][y] = '#'
                ship.location.append((position[0],y))
        elif ship.orientation == 'v':
            for x in range(position[0],position[0]+ship.size):
                grid.board[x][position[1]] = '#'
                ship.location.append((x,position[1]))

    grid.print_board()
    print('\n')
        
def check_position(grid, ship, position, orientation):
    """Checks to make sure that each computer ship is on the board doesn't collide with another. 
    
    Args:   
        The board of play, a ship, its orientation, and the proposed position of the ship.
        
    Returns:
        A possibly new position.
    """
    #Corrects positioning off the field of play.
    while position[1]+ship.size > grid.size-1 or position[0] + ship.size > grid.size-1:
        position = (random.choice([i for i in range(0,grid.size)]),random.choice([i for i in range(0,grid.size)]))
    
    #Corrects collision with another ship.       
    if orientation == 'h':
        while '#' in [grid.board[position[0]][y] for y in range(position[1],position[1]+ship.size)]:
            position = (random.choice([i for i in range(0,grid.size)]),random.choice([i for i in range(0,grid.size)]))
    elif orientation == 'v':
       while '#' in [grid.board[x][position[1]] for x in range(position[0],position[0]+ship.size)]:
            position = (random.choice([i for i in range(0,grid.size)]),random.choice([i for i in range(0,grid.size)]))
            
    return position
    
def attack_phase(ships, grid):
    """Controls the attack sequence of the user until he/she sinks all the computer's ships. 
    
    Args:   
        The board of play.
        
    Returns:
        None
    """
    positions_attacked = [] #Tuple of each position chosen.
    result_of_attack = [] #Result of attack.
    rounds = 0
    flag = True
    
    while flag==True:
        #User picks a random spot to attack.
        print('Choose a spot to attack. Here are your previous attacks: \n')
        print(zip(positions_attacked,result_of_attack))
        print('\n')
        grid.print_board() #For testing purposes. Remove for the real game.
        print('\n')
        x = int(raw_input('Which x position (between 0 and 9) do you want to attack? '))
        while x not in range(0,10):
            x = int(raw_input('Pick a position between 0 and 9 for x? '))
        y = int(raw_input('Which y position (between 0 and 9) do you want to attack? '))
        while y not in range(0,10):
            y = int(raw_input('Pick a position between 0 and 9 for x? '))
        while (x,y) in positions_attacked:
            print('You already attacked this position. Maybe you should choose another spot.\n')
            x = int(raw_input('x: '))
            y = int(raw_input('y: '))
            
        positions_attacked.append((x,y))
        print('\n')
        
        if grid.board[x][y] == '#':
            print("It's a hit.\n")
            result_of_attack.append('hit')
            grid.board[x][y] = 'X'
            check_sink(x,y,ships,grid)
        else:
            print('You missed.\n')
            result_of_attack.append('miss')
        
        rounds+=1
        list_check = [pos for col in grid.board for pos in col]
        if '#' not in list_check:
            grid.print_board()
            print("\n\nYou sank all the computer's ships.")
            flag = False
            
    print("\nSTATISTICS: You took "+str(rounds)+" rounds to sink the computer's ships.")  
    
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
        print("You sank the computer's {}".format(hit_ship.name))
        print('\n')   
    
        
    
    