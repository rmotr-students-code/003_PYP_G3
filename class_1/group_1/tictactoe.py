from __future__ import print_function

PLAYER1 = "X"
PLAYER2 = "O"
EMPTY = " "

def newGame(board):
    currentPlayer = PLAYER1
    while True:
        # Main game logic/loop
        printBoard(board)
        
        # Ask current player for move
        makeMove(currentPlayer)
        
        # Check if the game has ended and announce winner/draw if so and break loop
        if isEnd(board):
            if winner == "":
                print("The game has ended in a draw!")
            else:
                print("The winner was player {}! Congratulations!".format(currentPlayer))
            print("Thank you for playing!")
            break
        
        # Change current player
        if currentPlayer == PLAYER1:
            currentPlayer = PLAYER2
        else:
            currentPlayer = PLAYER1
    pass


def makeMove(player):
    # Ask for move and attempt it, repeat until successful
    while True:
        playerMove = input("Player {}, what is your move? ".format(player))
        try:
            row = playerMove[0]
            col = playerMove[1]
            if board[row][col] == EMPTY:
                board[row][col] = player
                print("Move successful.")
                return
            else:
                print("Invalid move, try again.")
        except:
            print("Invalid move, try again.")

def diag(board, reverse=False):
    diag = []
    for i in range(len(sorted(board))):
        board_keys = sorted(board.keys())
        if reverse:
            board_keys.reverse()
        col = board_keys[i]
        row = board[col]
        row_item = sorted(row.keys())[i]
        diag.append(board[col][row_item])
    return diag


def isEnd(board):
    # Check if the game has ended and return winner if end
    global winner
    boardFull = True
    
    # Check rows
    for row in board.values():
        row = list(row.values())
        if EMPTY not in row:
            if not (PLAYER1 in row and PLAYER2 in row):
                winner = row[0]
                return True
        else:
            boardFull = False
    
    # Check cols
    cols = list(board.values())[0]
    for col in cols:
        column = []
        for row in board.values():
            column.append(row[col])
        if EMPTY not in column:
            if not (PLAYER1 in column and PLAYER2 in column):
                winner = column[0]
                return True
        else:
            boardFull = False
    
    # Check diags
    right = diag(board)
    left = diag(board, reverse=True)
    if EMPTY not in right:
        if not (PLAYER1 in right and PLAYER2 in right):
            winner = right[0]
            return True
    else:
        boardFull = False
    
    if EMPTY not in left:
        if not (PLAYER1 in left and PLAYER2 in left):
            winner = left[0]
            return True
    else:
        boardFull = False
        

    
    return boardFull
#print(isEnd(board))



'''
def winner(board):
    # Return the winner
    pass
'''

def printBoard(board):
    n = len(board.keys())
    print(end='   ')
    for col in sorted(list(board.values())[0]):
        print(col, end=' ')
    print('\n  --+' + '-+'*(n-2) + '--')
    for row in sorted(board):
        print(row + ' |', end='')
        for col in sorted(board[row]):
            print(board[row][col], end='|')
        print('\n  --+' + '-+'*(n-2) + '--')

def generateBoard(rows="ABC", cols="123"):
    if len(rows) != len(cols):
        return None
    board = {}.fromkeys(rows)
    for row in rows:
        board[row] = {}.fromkeys(cols, " ")
 
    return board
    
#print(generateBoard())
#printBoard(generateBoard("ABCDE", "12345"))

input("Welcome to Tic-Tac-Toe. Press ENTER to start.")
#board = generateBoard("ABCD", "1234")
board = generateBoard()
newGame(board)