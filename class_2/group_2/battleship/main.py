# -*- coding: utf-8 -*-

# Battleship for rmotr class 2
# By Ross and Eloi

BOARD_SIZE = 10
# -- Import
import board
import craft
import mode
import player
import stats

# -- Global variables
board_inplay = board.create_board(BOARD_SIZE)
player_name = player.enter_name()
game_mode = player.player_mode(player_name)
ships = craft.create_ships()
stats = stats.create_stats()


if game_mode == "attack":
    print "Attack"
    mode.attack_mode(player_name, board_inplay, ships)
elif game_mode == "defend":
    print "Defend"
    mode.defend_mode(player_name, board_inplay, ships)

# player.game_over(board, mode, player, stats)
    








