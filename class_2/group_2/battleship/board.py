# -*- coding: utf-8 -*-

""" This file handles all of the board related functions """

#-- Import
from __future__ import print_function
import string

def create_board(size):
    """Return a dictionnary with a tuple of col and row as key and None as value"""
    board = {}
    for row in range(size):
        for col in range(size):
            board[(col, row)] = [None, None]
    return board

def print_board(board, mode):
    """ Print the board to the screen with different mode : setup, attack, defend"""
    print (" " * 3, end="")
    for i in range(10):
        print (" ", string.ascii_uppercase[i], end=" ")
    print ("")
    for row in range(10):
        print ("", end=" ")
        print (row + 1, " " * (2 - (row + 1) / 10), end="")
        for col in range(10):
            if mode == "setup":
                if board[(row, col)][0] == None:
                    print (" ", end=" ")
                else:
                    print (board[(row, col)][0], end=" ")
            elif mode == "attack":
                if board[(row, col)][1] == None:
                    print (" ", end=" ")
                else:
                    print (board[(row, col)][1], end=" ")
            elif mode == "defend":
                if board[(row, col)][1] != " ":
                    if board[(row, col)][1] == None:
                        print (" ", end=" ")
                    else:
                        print (board[(row, col)][1], end=" ")
                else:
                    if board[(row, col)][0] == None:
                        print (" ", end=" ")
                    else:
                        print (board[(row, col)][0], end=" ")
            if col != 9:
                print ("|", end=" ")
        if row != 9:
            print ("\n", " " * 4, "---+" * 9, "---", sep="")
    print ("\n")


def update_board(board, move):
    if board[move][0] == None:
        board[move][1] = 'M'
        print ("Bad luck you missed!")
        return 'M'
    else:
        board[move][1] = 'H'
        print ("Well done you had a hit!")
        return 'H'


def place_ship(board, ship, position, ships, ship_name):
    """ Place ships at the start of the game"""
    starting_position_col = position[0][0]
    starting_position_row = position[0][1]
    direction = position[1]
    
    if direction == 'V':
        if starting_position_col + ship['length'] > 9:
            print ("Your ship is out of the board, try another position")
            return False
        else: 
            for i in range(ship['length']):
                if board[(starting_position_col + i, starting_position_row)][0] != None:
                    print ("Your ship colide another ship, try another position")
                    return False
    else:
        if starting_position_row + ship['length'] > 9:
            print ("Your ship is out of the board, try another position")
            return False
        else:
            for i in range(ship['length']):
                if board[(starting_position_col, starting_position_row + i)][0] != None:
                    print ("Your ship colide another ship, try another position")
                    return False
    
    ships[ship_name]['direction'] = direction
    ships[ship_name]['start_position'] = (starting_position_col, starting_position_row)
    
    if direction == 'V':
        for i in range(ship['length']):
            board[(starting_position_col + i, starting_position_row)][0] = ship['symbol']
    else:
        for i in range(ship['length']):
            board[(starting_position_col, starting_position_row + i)][0] = ship['symbol']
    return True
    