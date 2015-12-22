"""
Fibonacci numbers: (http://en.wikipedia.org/wiki/Fibonacci_number)

Write a program that generates the nth number in a fibonacci sequence (starting at 0). The program should start and ask two things:

    The number that will describe the nth term you want to get
    if the function should be recursive or not

The program should count with data validation. It means that the program must inform the user when the number she inserted is invalid.

Extra: If the user passes a --recursive argument, the program should not ask for the function to use and use the recursive function.
"""
#fib(13) = 233
#fib(29) = 514229

import sys

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

def fibr(n):
    if n <= 1:
        return n
    else:
        return fibr(n-1) + fibr(n-2)        


if __name__ == '__main__':
    '''
    This could be tidied up a bit
    '''
    
    n = int(raw_input('Please enter the position in the fibonacci sequeuce you would like: '))
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--recursive':
            recursive = True
    else:
        user_recursive = raw_input('Would you like to use a recursive algorithm? ')
        if user_recursive.lower() == 'yes':
            recursive = True
        else:
            recursive = False
        
    
    if recursive:
        print fibr(n)
    else:
        print fib(n)