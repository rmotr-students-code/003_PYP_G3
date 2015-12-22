"""Controls the defence workflow of the game."""

import random

def computer_attacks(grid,ships):
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
        #Directed AI attack.
        #if len(positions_attacked) > 0:
        #    if result_of_attack[-1] == 1:
        #        ref = positions_attacked[-1]
        #        targeted_grid = [(ref[0]-1,ref[1]),(ref[0],ref[1]-1),(ref[0]+1,ref[1]),(ref[0],ref[1]+1)]
        #        guess = random.choice(targeted_grid)
        #        while guess in positions_attacked:
        #            check = [True for pos in targeted_grid if pos in positions_attacked]
        #            if len(check) == len(targeted_grid):
        #                break
        #            guess = random.choice(targeted_grid)
        #        positions_attacked.append(guess)
        
        #AI picks a random spot to attack.
        #else:
        guess = (random.choice([i for i in range(0,10)]), random.choice([i for i in range(0,10)]))
        while guess in positions_attacked:
            guess = (random.choice([i for i in range(0,10)]), random.choice([i for i in range(0,10)]))
        positions_attacked.append(guess)
        
        print('\n')
        print_board(grid)
        print('\n')
        
        print('I guess '+str(guess)+'. Did I hit, miss or sink a ship? \n')
        user_answer = raw_input("Type 'h' (hit), 'm' (miss) or 's' (sink): ").lower() #need to add sink option
        while user_answer not in ['h','s','m']:
            user_answer = raw_input("Please type 'h' (hit), 'm' (miss) or 's' (sink): ")
        print('\n')
            
        if grid[guess[0]][guess[1]] == '#':
            if user_answer == 'm':
                print("You're lying."), #Didn't bother with other variations of lying. Not worth the time. 
            print("Hit.\n")
            result_of_attack.append(1)
            grid[guess[0]][guess[1]] = 'X'
            check_sink(guess[0],guess[1],ships,grid)
        else:
            print('Missed.\n')
            result_of_attack.append(0)
        
        rounds+=1
        list_check = [pos for col in grid.values() for pos in col]
        if '#' not in list_check:
            print('The computer has sunken all your ships.')
            flag = False
    
    print('\nSTATISTICS: The computer took '+str(rounds)+' rounds to sink all your ships.')        

def check_sink(x,y,ships,grid):
    """Checks to see if a ship has been sunk.
    
    Args:   
        The x and y position of the hit and the computer's ships.
        
    Returns:
        Whether or not a ship has sunk.
    """
    hit = (x,y)
    for ship in ships:
        if hit in ship['location']:
            hit_ship = ship
            
    sunk_check = set([grid[i[0]][i[1]] for i in hit_ship['location']])
    
    if sunk_check == set(['X']):
        print("The computer sank your {}".format(hit_ship['name']))
        print('\n')

def defend(user_ships,grid):
    """Controls the setup of the game for the user's defence. 
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    print_board(grid)
    print('\n')
    print('The board is a 10x10 grid labelled 0-9 on both sides. You have 4 ships: A submarine of size 3, an aircraft of size 5 and two patrol boats of size 2. Choose the orientation (horizontal or vertical) of your ships. \n')
    set_position_orientation(user_ships,grid)
    computer_attacks(grid,user_ships)
   
def set_position_orientation(user_ships,grid): 
    """Sets the user's ships on the board. 
    
    Args:   
        The board of play and the user's ships.
        
    Returns:
        None
    """
    #Assigns an orientation and position to every ship
    for ship in user_ships: 
        orientation = raw_input("Do you want the orientation of the "+ship['name']+" to be vertical or horizontal? Enter 'h' for horizontal and 'v' for vertical: ")
        while orientation not in ('h','v'):
            orientation = raw_input("Please enter either 'h' for horizontal and 'v' for vertical: ")
            
        x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
        while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
        x = int(x)
            
        y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
        while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
        y = int(y)
        position = (x,y)
        position = check_position_orientation(grid, ship, position, orientation)
        ship['orientation'] = orientation
        ship['position'] = position
        
        #Fills the spaces occupied by each ship with an 'X' and logs these spaces for each ship as its position.
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
    """Checks to make sure that each user ship is on the board and doesn't collide with another. 
    
    Args:   
        The board of play, a ship, its orientation, and the proposed position of the ship.
        
    Returns:
        A possibly new position.
    """
    #Corrects positioning off the field of play.
    if orientation == 'h':
        while position[1]+ship['size']>10:
            print('The ship is off board. Enter new positions')
            print_board(grid)
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            y = int(y)
            position = (x,y)
    elif orientation == 'v':
        while position[0]+ship['size']>10:
            print('The ship is off board. Enter new positions')
            print_board(grid)
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            y = int(y)
            position = (x,y)
            
    
    #CODE BELOW THREW AN ERROR ONCE. LOOK OUT.
    #Corrects collison with another ship.      
    if orientation == 'h':
        while '#' in [grid[position[0]][y] for y in range(position[1],position[1]+ship['size'])]:
            print('The ship collides with another. Enter new positions')
            print_board(grid)
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            y = int(y)
            position = (x,y)
    elif orientation == 'v':
       while '#' in [grid[x][position[1]] for x in range(position[0],position[0]+ship['size'])]:
            print('The ship collides with another. Enter new positions')
            print_board(grid)
            print('\n')
            x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while x not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                x = raw_input('Which x position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            x = int(x)
            
            y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            while y not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                y = raw_input('Which y position (between 0 and 9) do you want to place the '+ship['name']+'? ')
            y = int(y)
            position = (x,y)
            
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
    