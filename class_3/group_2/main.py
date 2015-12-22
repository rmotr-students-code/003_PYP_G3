#-- Imports
import board
import player
import ship

#-- Constants
SUBMARINE = 'SUBMARINE'
AIRCRAFT = 'AIRCRAFT'
PATROL1 = 'PATROL1'
PATROL2 = 'PATROL2'
SHIPS = [SUBMARINE, AIRCRAFT, PATROL1, PATROL2]

ship_list = []
for a_ship in SHIPS:
	a_ship = ship.Ship(a_ship)
	ship_list.append(a_ship)

cpu_board = board.Board()
player_board = board.Board()
cpu = player.ComputerPlayer(cpu_board , 'CPU')
player_one = player.HumanPlayer(player_board, 'player 1')
player_one.place_ship(ship_list)
