import board
import ship
import player


def mainGameLoop(firstPlayer, secondPlayer, mode="standard"):
    while True:
        # First player turn
        if mode == "standard" or mode == "attack":
            # Ask player for move
            firstPlayer.makeMove(secondPlayer.get_board())
            
            # Check if the game has ended, break if so
            if secondPlayer.get_board().endGame():
                print("{} wins!".format(firstPlayer))
                break
        
        # Second player turn
        if mode == "standard" or mode == "defend":
            # Ask for other player move (computer)
            secondPlayer.makeMove(firstPlayer.get_board(), promptPlayer=mode=="defend")
            
            # Check if the game has ended, break if so
            if firstPlayer.get_board().endGame():
                print("{} wins!".format(secondPlayer))
                break
        print("\nEnd of round\n" + "-"*30 + "\n")


def newGame(mode="standard"):
    '''
    
    '''
    firstPlayerBoard = board.Board()
    firstPlayer = player.HumanPlayer(firstPlayerBoard, "Human player")
    secondPlayerBoard = board.Board()
    secondPlayer = player.ComputerPlayer(secondPlayerBoard, "ComputerPlayer")
    
    if mode == "standard" or mode == "defend":
        firstPlayer.setup()
    
    if mode == "standard" or mode == "attack":
        secondPlayer.setup()
    
    return [firstPlayer, secondPlayer]
    
print('Welcome to Battleship!')
mode = input('What mode do you want to play ("standard", "attack", "defend")? ')
mode = mode.lower()
if mode not in ["standard", "attack", "defend"]:
    print('You have chosen an invalid mode. Mode is defaulted to "standard"')
    mode = "standard"
players = newGame(mode)
mainGameLoop(players[0], players[1], mode)