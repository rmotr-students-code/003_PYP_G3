# -*- coding: utf-8 -*-

""" This file handles all of the move logic """

import random
import string
import board

# **** ATTACK ****
# The user will enter their coordinates
# The computer will check if the coordinates have a ship on them.
# The computer will check if the ship that it has hit still has remaining spaces that can be hit. 
# The computer will inform the user if the hit was: A Hit (H) because the ship it hit had more spaces left to be hit; A Miss(M) because no ships exist in the space, or if it resulted in a Sunk(X) because a ship existed in the space AND had no more spaces left to be hit.
# The computer then reprints the board with the result of the go displayed on the board using X, H, M.
# The computer checks if any ships are still unsunk.  
# If there are are then the game continues using steps 2 - 7.  
# If all ships are sunk it will end the game and print out statistics
    
def player_move(player_name, board_inplay):
    """ This handles the attack move logic.  Returns the result of the move as either 
    invalid, Hit, Miss, or Sunk"""
    while True:
        user_move = raw_input((" Please enter your move {} by entering a letter and a number (e.g. A2, G3): ").format(player_name))
        user_col = user_move[0].upper()
        user_row = int(user_move[1:]) - 1
        if user_col not in string.ascii_uppercase[:10] or \
            user_row not in range(10):
            print "You can only enter a letter between A - J followed by a number between 1 - 10"
            continue
        else:
            valid_user_move = (user_row, ord(user_col) - 65)
            if board_inplay[valid_user_move][1] == None:
                return valid_user_move
            else:
                if board_inplay[valid_user_move][1] == 'H':
                    print "{} already has a hit on it. Try again!".format(user_move)
                    continue
                elif board_inplay[valid_user_move][1] == "M":
                    print "You already missed at {}. Try again!".format(user_move)
                    continue
                elif board_inplay[valid_user_move][1] == "X":
                    print "{} already has a sunken ship on it. Try again!".format(user_move)

# **** DEFEND ****
# The user informs the computer of the above result based on the layout of their board.
# If the result is a Hit the computer will store the result in memory (so that it doesn’t ask for the same co-ordinates again) and will then try and attack the nearest neighbours on subsequent goes repeating steps 1 & 2 until it achieves a Sunk result for that ship.
# If the result is a Miss the computer will store the coordinates in memory (so that it doesn’t ask for the same co-ordinates again) and will then try another available random coordinates within the grid using steps 1 & 2
# The computer checks the actual position on the board to verify that the value is as the user input.  If the values do not match the computer lets the user know they are cheating.
# (optional) - if it finds out you are cheating it will sink an active ship
# The computer stores a sunk ship in to memory so that it knows what shapes of ship are left
# The computer will check to see if all of the ships have been sunk.  If this is equal to False it will repeat steps 1-5.
# Once all ships are sunk the computer will finish the game

def ask_ship_position():
    while True:
            ship_position = raw_input("Please enter the starting position of your ship : ")
            user_col = ship_position[0].upper()
            user_row = int(ship_position[1:]) - 1
            if user_col not in string.ascii_uppercase[:10] or \
                user_row not in range(10):
                print "You can only enter a letter between A - J followed by a number between 1 - 10"
                continue
            else:
                valid_user_move = (user_row, ord(user_col) - 65)
                ship_direction = None
                while ship_direction != 'H' and ship_direction != 'V':
                    ship_direction = raw_input("Please enter the orientation of your ship (H for Horizontal or V for Vertical) : ")
                    if ship_direction != 'H' and ship_direction != 'V':
                        print ("Please enter a valid orientation")
                    else:
                        return valid_user_move, ship_direction
                        
                    
                
                
                    

def cpu_move(board_inplay):
    """ This handles the defend move logic. Returns the result of the move as either 
    invalid, Hit, Miss, or Sunk"""

    # Generate a random coordinate number (e.g. 0, 8)  within the 
    # bounds of the board and asks the user if the position is either a Hit, Miss, or Sunk.
    """
    available_positions = {key:value for key, value in board.iteritems() if None in value}
    cpu_move = random.sample(available_positions, 1)
    """
    available_positions = board_inplay.keys()
    random.shuffle(available_positions)

    return available_positions.pop()





    
    
