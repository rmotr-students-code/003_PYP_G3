#Redoing battle ship using OOP.
import sys
from attack_OOP import attack
from defend_OOP import defend

def main():
    if sys.argv[1] == '--attack':
        attack()
    elif sys.argv[1] == '--defend':
        defend()
    else:
        print('Stop screwing around.')
        exit(1)

if __name__ == "__main__":
    main()
        
    
