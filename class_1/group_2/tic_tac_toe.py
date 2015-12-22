

columns = ("a", "b", "c")
rows = ("1", "2", "3")


def prompt():
    print "You need to enter a value consisting of a \nletter and then a number - e.g. A1, B2, C3"
    
    
def move(board, player):
    while True:
        
        go = user_go(player)
        if board[go] == None:
            board[go] = player
            return board
        else:
            print "This place is already taken.  Please choose a different one"

def user_go(player):
    formatted = False
    while  formatted == False:
        go = raw_input("\n\n{} please enter your move: ".format(player))
        if len(go) == 2:
            go = go.lower()
            if go[0] in columns:
                if go[0] == "a":
                    go_column = 0
                elif go[0] == "b":
                    go_column = 1
                elif go[0] == "c":
                    go_column = 2
                else:
                    prompt()
                    continue
                if go[1] in rows:
                    go_row = int(go[1]) - 1
                    formatted = True
                    return go_column, go_row
                else:
                    prompt()
                    continue
            else:
                prompt()
                continue
        else:
            prompt()
            continue
            
        
def align_horizontaly(board):
    for j in range (3):
        last_value = None
        same_value_in_a_row = 0
        for i in range (3):
            if last_value != None and board[(i, j)] == last_value:
                same_value_in_a_row += 1
            last_value = board[(i, j)]
            if same_value_in_a_row == 2:
                return last_value
        return False

def align_verticaly(board):
    for i in range (3):
        last_value = None
        same_value_in_a_row = 0
        for j in range (3):
            if last_value != None and board[(i, j)] == last_value:
                same_value_in_a_row += 1
            last_value = board[(i, j)]
            if same_value_in_a_row == 2:
                return last_value
        return False

def align_diagonal(board):
    if (board[(0, 0)] == board[(1, 1)] == board[(2, 2)]) \
    or (board[(0, 2)] == board[(1, 1)] == board[(2, 0)]):
        return board[(1, 1)]
    else:
        return False
        

def create_board():
    print """
    Welcome to Tic Tac Toe.  The game of War!
    To start the war please enter a move by using
    a combination of a letter and then a number.
    E.g. A1, B2, C3
            
             A   B   C 
        1      |   |
            ---+---+---
        2      |   |   
            ---+---+---
        3      |   |
               
               
               
    """
    board = {}
    for j in range(3):
        for i in range(3):
            board[(i, j)] = None
    return board

def print_board(board, players):
    print "\n     A   B   C "
    for j in range(3):
        print j + 1, "  ",
        for i in range(3):
            if i == 2:
                if (board[(i, j)]) == players[0]:
                    print "X",
                elif (board[(i, j)]) == players[1]:
                    print "O",
                else:
                    print " ",
            else:
                if (board[(i, j)]) == players[0]:
                    print "X",
                elif (board[(i, j)]) == players[1]:
                    print "O",
                else:
                    print " ",
                print"|",
        if j == 2:
            print "\n"
        else:
            print "\n    ---+---+---"
    

def winner(board, player):
    if align_horizontaly(board):
        return align_horizontaly(board)
    elif align_verticaly(board):
        return align_verticaly(board)
    elif align_diagonal(board):
        return align_diagonal(board)
    else:
        return False


def tic_tac_toe():
    board = create_board()
    players = []
    players.append(raw_input("Please enter player 1 name (X): "))
    players.append(raw_input("Please enter player 2 name (O): "))
    print "\n\nWelcome {} and {}. Let's play!".format(players[0], players[1])
    player = players[0]
    turn = 1
    while turn < 9 and winner(board, players) == False:
        print_board(board, players)
        go = move(board, player)
        player = players[0] if player == players[1] else players[1]
        turn += 1
    result = winner(board, players)
    if result: 
        print "Well done! {} won the game".format(result)
        print print_board(board, players)
    else:
        print "That's the end of the game!"
        print print_board(board, players)

tic_tac_toe()