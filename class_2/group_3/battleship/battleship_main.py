import sys
from copy import deepcopy
from defend import defend
from attack import attack

#Generates a 10*10 dictionary, assigning each position.
grid = {i: ['_']*10 for i in range(10)} 

#Dictionary for ship, size, position and orientation
ships = [{'name': 'submarine', 'size': 3, 'position': ' ','orientation': ' '}, 
        {'name': 'aircraft', 'size': 5, 'position': ' ','orientation': ' '},
        {'name': 'patrol_boat', 'size': 2, 'position': ' ','orientation': ' '}, 
        {'name': 'patrol_boat', 'size': 2, 'position': ' ','orientation': ' '}] 
        
#Forms a copy of this ship dictionary, for the computer and user.       
user_ships = deepcopy(ships) 
computer_ships = deepcopy(ships) 

def main():
    """Starts the game and sees whether the user will be attacking or defending.
    
    Args:   
        None
        
    Returns:
        None
    """
    global grid, user_ships, computer_ships

    if sys.argv[1] == '--attack':
        attack(computer_ships,grid)
    elif sys.argv[1] == '--defend':
        defend(user_ships,grid)
    else:
        print('Stop screwing around')
        exit(1)

if __name__=='__main__':
    main()

