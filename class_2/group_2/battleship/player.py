# -*- coding: utf-8 -*-

""" This file handles all of the player related functions """


def enter_name():
    """ Asks the user to enter their name"""
    player_name = raw_input("Welcome player.  Please enter your name: ")
    return player_name
    

def player_mode(name):
    """ 
    Asks the player to choose a mode for the game. (Either "Attack" or "Defend")
    TODO: Check if a user enters anything but a 1 or a 2
    """
    
    mode = 0
    
    print """
    *** Please choose a game mode {} ***
    
    Press 1 for "Attack"
    Press 2 for "Defend"
    """.format(name)
    
    while mode == 0:
        try: 
            user_input = int(raw_input("Please enter your choice: "))
            if user_input == 1 or user_input == 2:
                if user_input == 1:
                    print "Thank you. You have chosen 'Attack' Mode"
                    mode = "attack"
                elif user_input == 2:
                    print "Thank you.  You have chosen 'Defend' Mode"
                    mode = "defend"
            else:
                print "You need to enter either a 1 or a 2"
        except:
            print "You can only enter a 1 or a 2"
    return mode


def game_over(board, mode, player, stats):
    print board
    print " The game is over {}".format(player)
    if mode == "attack":
        print " \nWell done for defeating me."
        print " *** See your stats below ***"
        print stats
    return

def move_confirmation():
    user_response = None
    while user_response == None:
        user_response = raw_input("Has the computer Missed (M), Hit (H) or Sunk (S) a ship?: ").upper()
        if user_response not in ['H', 'M', 'S']:
            user_response = None
        else:
            return user_response

    
if __name__ == '__main__':
    player_mode()
    