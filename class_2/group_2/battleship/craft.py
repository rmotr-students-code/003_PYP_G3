# -*- coding: utf-8 -*-

""" This file handles all of the ship related functions."""


def attack_ship(position, ships):
    """ This updates a ship when it is attacked"""
    pass

        
def create_ships():
    """ This creates a dictionary of ships to be used in the game"""
    ships = {   'submarine': {
                    'start_position':   None,
                    'direction':        None,
                    'sunk':             False,
                    'length':           3,
                    'symbol':          'S'
                },
                'aircraft': {
                    'start_position':   None,
                    'direction':        None,
                    'sunk':             True,
                    'length':           5,
                    'symbol':          'A'
                },
                'patrol_boat1': {
                    'start_position':   None,
                    'direction':        None,
                    'sunk':             False,
                    'length':           2,
                    'symbol':          '1'
                },
                'patrol_boat2': {
                    'start_position':   None,
                    'direction':        None,
                    'sunk':             False,
                    'length':           2,
                    'symbol':          '2'
                },
            }
            
    return ships
    

def ships_available(ships):
    """ Checks to see if all ships have been sunk or not. Return True if ships 
    are still available to be sunk."""
    if ships['submarine']['sunk'] == False \
        or ships['submarine']['sunk'] == False \
        or ships['aircraft']['sunk'] == False \
        or ships['patrol_boat1']['sunk'] == False \
        or ships['patrol_boat2']['sunk'] == False:
        return True
    else:
        return False
    pass


def sink_all_ships(ships):
    """ This is an easter egg that sinks all ships when a user types 
    'armegeddon' in to the move.  The game automatically ends with a 
    custom message"""
    pass


def update_sunk_status(board, ships):
    ships_name = ships.keys()
    ships_not_sunk = [ship_name for ship_name in ships_name if ships[ship_name]['sunk'] == False]
    for ship in ships_not_sunk:
        if is_sunk(board, ship):
            ship['sunk'] = True


def is_sunk(board, ship):
    col = ship['start_position'][0]
    row = ship['start_position'][1]
    
    if ship['direction'] == 'H':
        for i in range(ship['length']):
            if board[(col, row + i)][1] != 'H':
                return False
    elif ship['direction'] == 'V':
            for i in range(ship['length']):
                if board[(col + i, row)][1] != 'H':
                    return False
    return True


if __name__ == "__main__":
    ships = create_ships()
    print ships_available(ships)
    
    
    
    