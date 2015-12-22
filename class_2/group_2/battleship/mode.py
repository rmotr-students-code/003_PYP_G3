# -*- coding: utf-8 -*-

""" This file handles all of the modes of the game and the function
calls they make and process to run the game"""

#-- Import
import board
import craft
import move
import random
import player

def attack_mode(player_name, board_inplay, ships):
    """ The attack mode game logic using function calls"""

    print "The computer placed his ships, try to sink them!" 
    for ship in ships.keys():
        available_positions = board_inplay.keys()
        random.shuffle(available_positions)
        direction = ['H', 'V']
        while (board.place_ship(board_inplay, ships[ship], (available_positions.pop(), random.choice(direction)), ships, ship) == False):
            pass
        
    print(chr(27) + "[2J")
    print "=" * 15, "Attack Mode", "=" * 15, "\n"
    print "The computer placed his ships, try to sink them!"
    board.print_board(board_inplay, 'setup')
    raw_input("Press enter to continue")
        
    turn = 0
    while craft.ships_available(ships):
        print(chr(27) + "[2J")
        turn += 1
        board.print_board(board_inplay, 'attack')
        user_move = move.player_move(player_name, board_inplay)
        board.update_board(board_inplay, user_move)
        for ship in ships:
            if craft.is_sunk(board_inplay, ships[ship]) and ships[ship]['sunk'] == False:
                ships[ship]['sunk'] = True
                if ships[ship]['sunk'] == True:
                    print ("Well played, you just sunk the computer's {}".format(ship))
    board.print_board(board_inplay, 'attack')
    print ("You beat the computer in {} moves".format(turn))


def defend_mode(player_name, board_inplay, ships):
    """ The defend mode game logic using function calls"""
    print "=" * 15, "Defend Mode", "=" * 15, "\n"
    
    for ship in ships.keys():
        board.print_board(board_inplay, 'setup')
        print "Please place the {} ship.".format(ship)
        while (board.place_ship(board_inplay, ships[ship], move.ask_ship_position(), ships, ship) == False):
            pass
    
    available_positions = board_inplay.keys()
    random.shuffle(available_positions)
    turn = 0 
    while craft.ships_available(ships):
        print(chr(27) + "[2J")
        last_mod = board.update_board(board_inplay, available_positions.pop())
        board.print_board(board_inplay, 'defend')
        turn += 1
        
        for ship in ships:
            if craft.is_sunk(board_inplay, ships[ship]) and ships[ship]['sunk'] == False:
                ships[ship]['sunk'] = True
                if ships[ship]['sunk'] == True:
                    last_mod = 'S'
        
        
        if last_mod == player.move_confirmation():
            print "I compute that"
        else:
            print "You lied"
        
    print ("Well played, you survived {} turns !".format(turn))