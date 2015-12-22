class Ship(object):
    orientation = ''
    location = []

        
class Aircraft(Ship):
    size = 5
    name = 'aircraft'

class PatrolBoat(Ship):
    size = 2
    name = 'patrol boat'

class Submarine(Ship):
    size = 3
    name = 'submarine'

    
class Grid(object):
    
    def __init__(self,x,y):
        self.board = [['_']*y for i in range(x)]
        self.size = x
        
    def place_ship(self):
        pass
        
    def print_board(self):
        for i in range(len(self.board)):
            print(str(i)+' '),
            for j in range(len(self.board[i])):
                print(self.board[i][j]+' | '),
            print('\n')
        for i in range(len(self.board)):
            if i == 0:
                print('   '+str(i)+'   '),
            else:
                print(str(i)+'   '),