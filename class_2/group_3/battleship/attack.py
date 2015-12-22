"""Controls the attack workflow of the game."""

import random

def user_attacks(grid,ships):
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
        print_board(grid) #For testing purposes. Remove for the real game.
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
        
        if grid[x][y] == '#':
            print("It's a hit.\n")
            result_of_attack.append('hit')
            grid[x][y] = 'X'
            check_sink(x,y,ships,grid)
        else:
            print('You missed.\n')
            result_of_attack.append('miss')
        
        rounds+=1
        list_check = [pos for col in grid.values() for pos in col]
        if '#' not in list_check:
            print_board(grid)
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
        if hit in ship['location']:
            hit_ship = ship
            
    sunk_check = set([grid[i[0]][i[1]] for i in hit_ship['location']])
    
    if sunk_check == set(['X']):
        print("You sank the computer's {}".format(hit_ship['name']))
        print('\n')
        

def attack(computer_ships,grid):
    """Controls the setup of the game for the computer's defence. 
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    print('Please wait while the computer places its ships. \n')
    set_position_orientation(computer_ships,grid)
    user_attacks(grid,computer_ships)
    
def set_position_orientation(computer_ships,grid): 
    """Sets the computer's ships on the board.
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    #Assigns an orientation and position to every ship.
    for ship in computer_ships: 
        orientation = random.choice(['h','v'])
        position = (random.choice([i for i in range(0,10)]),random.choice([i for i in range(0,10)]))
        position = check_position_orientation(grid, ship, position, orientation)
        ship['orientation'] = orientation
        ship['position'] = position
        
        #Fills the spaces occupied by each ship with an 'X'.
        ship['location'] = []
        if ship['orientation'] == 'h':
            for y in range(position[1],position[1]+ship['size']):
                grid[position[0]][y] = '#'
                ship['location'].append((position[0],y))
        elif ship['orientation']== 'v':
            for x in range(position[0],position[0]+ship['size']):
                grid[x][position[1]] = '#'
                ship['location'].append((x,position[1]))

    print_board(grid)
    print('\n')
        
def check_position_orientation(grid, ship, position, orientation):
    """Checks to make sure that each computer ship is on the board doesn't collide with another. 
    
    Args:   
        The board of play, a ship, its orientation, and the proposed position of the ship.
        
    Returns:
        A possibly new position.
    """
    #Corrects positioning off the field of play.
    while position[1]+ship['size']>9 or position[0]+ship['size']>9:
        position = (random.choice([i for i in range(0,10)]),random.choice([i for i in range(0,10)]))
    
    #CODE BELOW THREW AN ERROR ONCE. LOOK OUT.
    #Corrects collision with another ship.       
    if orientation == 'h':
        while '#' in [grid[position[0]][y] for y in range(position[1],position[1]+ship['size'])]:
            position = (random.choice([i for i in range(0,10)]),random.choice([i for i in range(0,10)]))
    else:
       while '#' in [grid[x][position[1]] for x in range(position[0],position[0]+ship['size'])]:
            position = (random.choice([i for i in range(0,10)]),random.choice([i for i in range(0,10)]))
            
    return position

def print_board(grid):
    """Prints the board of play.
    
    Args:   
        None
        
    Returns:
        None
    """
    for key in grid.keys():
        print(str(key)+'  '),
        for val in grid[key]:
            print(val+' | '),
        print('\n')
        
    for i in range(0,10):
        if i == 0:
            print('    '+str(i)+'   '),
        else:
            print(str(i)+'   '),