#A dictionary outlining the positions on the 3x3 board.
positions = {'A1': '_','A2': '_', 'A3': '_',
            'B1': '_','B2': '_', 'B3': '_', 
            'C1': '_','C2': '_', 'C3': '_'}
            
def printboard():
    """Outputs a visual representation of the board.
    
    Args:
        None
        
    Returns:
        None
    """
    print(positions['A1']+' | '+positions['A2']+' | '+positions['A3'])
    print(positions['B1']+' | '+positions['B2']+' | '+positions['B3'])
    print(positions['C1']+' | '+positions['C2']+' | '+positions['C3'])

def check_win():
    """Checks to see if someone has won.
    
    Args:  
        None
        
    Returns:
        If someone won, the set containing the winning symbols - X for player 1, O for player 2.
        Else an arbitrary symbol is sent back to tell the program to continue.
    """
    #Every winning combination on a 3x3 board stored as sets in a list.
    #Using sets allows easy checking of whether or not all three positions have the same value.
    possible_wins = [set([positions['A1'],positions['A2'],positions['A3']]),
                set([positions['B1'],positions['B2'],positions['B3']]),
                set([positions['C1'],positions['C2'],positions['C3']]),
                set([positions['A1'],positions['B1'],positions['C1']]),
                set([positions['A2'],positions['B2'],positions['C2']]),
                set([positions['A3'],positions['B3'],positions['C3']]),
                set([positions['A1'],positions['B2'],positions['C3']]),
                set([positions['C1'],positions['B2'],positions['A3']])]
    
    for win in possible_wins:
        if len(win)==1 and '_' not in win:
            return win
            
    return set('+')
    
def check_valid_move(input_move):
    """Checks to see if a valid move was played.
    
    Args:  
        The input move of a player
        
    Returns:
        The original move if it was valid. A new valid move if not.
    """
    #Check to see if the player stayed on the 3x3 board in his/her move choice.
    if input_move not in positions.keys():
        while True:
            input_move = raw_input('That position is not on the board. Please enter a valid move: ')
            if input_move in positions.keys():
                break
    
    #Checks to make sure that the player's move is an unoccupied spot.
    if positions[input_move]!='_':
        while True:
            input_move = raw_input('That position is already filled. Please enter a valid move: ')
            if positions[input_move]=='_':
                break
            
    return input_move
    
def main():
    """Runs the game."""
    
    printboard()
    counter = 0 #Keeps track of the rounds to see when a draw is reached.
    print "Players get ready!"
    
    while True:
        
        counter += 1
        print "Round {}".format(counter)
        
        player_1 = raw_input("Player 1: ")
        player_1 = check_valid_move(player_1)
        positions[player_1] = 'X'
        printboard()
        
        win = check_win()
        if 'X' in win:
            print 'Player 1 wins'
            break
        elif 'O' in win:
            print 'Player 2 wins'
            break
        
        counter += 1
        print "Round {}".format(counter)
        
        player_2 = raw_input("Player 2: ")
        player_2 = check_valid_move(player_2)
        positions[player_2] = 'O'
        printboard()
        
        win = check_win()
        if 'X' in win:
            print 'Player 1 wins'
            break
        elif 'O' in win:
            print 'Player 2 wins'
            break
        
        
        
        #After 5 rounds of play, i.e. counter = 6, the board is filled so it's a draw.
        if counter == 10:
            print "It's a draw"
            break
        
if __name__=='__main__':
    main()