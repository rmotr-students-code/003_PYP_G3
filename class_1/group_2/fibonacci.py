"""
A programme to work out the nth number of a Fibonacci sequence.

The function takes 1 optionw (nth number) and one flag (--recursive).

The programme must ask a user for an integer and what function type they 
wish to use.  If they use the --recusive flag the programme will 
only ask for an integer.

Fibonacci uses the algorythmn F_n = F_{n-1} + F_{n-2}.

The function starts at 0 for the Fibonacci sequence 
so it = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

"""
import sys

def fibonacci_iterative(number): 
    fibonacci_sequence = [0, 1] # I've changed the name of the variable so it's now self explanatory
    
    i = 2    
    if number > 1:
        while i < number:
            fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
            i += 1
    return fibonacci_sequence[number-1]
        
def fibonacci_recursive(n, n_1, number): # I've not modified how the function work but I've found more explicit way to wright it
    while number !=1:
        number = number - 1
        fibonacci_recursive(n_1, n + n_1, number)
    return n
    
number = None

while number == None or number < 1:
    try:
        number = int(raw_input("Please enter a number: "))
    except:
        print "You must enter an integer"
    
try:
    if sys.argv[1] == '--recursive':
        print(fibonacci_recursive(0, 1, number))
except IndexError:
    while True:
        recursive = raw_input("Do you want it to be recursive or not? y/n ")
        recursive = recursive.lower()
        if recursive == 'y':
            print(fibonacci_recursive(0, 1, number))
            sys.exit()
        elif recursive == 'n':
            print(fibonacci_iterative(number))
            sys.exit()
        else:
            print "You must enter either y or n"
    
                
        
        





