#Fibonacci
import sys

def which_fib(n,func = 'n'):
    """Chooses whether or not to use a nonrecursive or recursive method to find the nth fibonacci number.
    
    Args:
        A number n and the method to be used, and 'n' or 'y', the first saying to use the nonrecursive function.
        
    Returns:
        The nth fibonacci number calculated by the chosen method.
    """
    
    if func == 'n':
        return nonrecursive_fib(n)
    else:
        return recursive_fib(n)
        
def nonrecursive_fib(n):
    """Computes the requested fibonacci number nonrecursively.
    
    Args:
        A number n
        
    Returns:
        The nth fibonacci number
    """
    
    fib1 = 0
    fib2 = 1
    counter = 2
     
    #base cases
    if n == 1: 
        return fib1
    if n == 2: 
        return fib2
     
    while counter < n:
        fib2, fib1 = fib1 + fib2, fib2
        counter+=1
        
    return fib2
        
def recursive_fib(n):
    """Computes the requested fibonacci number recursively.
    
    Args:
        A number n
        
    Returns:
        The nth fibonacci number
    """
    
    #base cases
    if n == 1: 
        return 0
    if n == 2: 
        return 1
        
    return recursive_fib(n-1) + recursive_fib(n-2)
        
        
def main():
    
    if len(sys.argv) > 1:
        if sys.argv[2] == '--recursive':
            print(recursive_fib(sys.argv[1]))
    else:
        user_query = int(raw_input('Please enter which Fibonacci number you want to find. '))
        user_choice = raw_input("Do you want to compute it recursively? Enter 'n' for no and 'y' for yes. ")
        print(which_fib(user_query,func=user_choice))
    
if __name__=='__main__':
    main()
     
     
     
        
