"""
Implement an @only_int_arguments decorator for the "sum_integers(*args)" function. It must
validate that all arguments passed to the function are integers, or raise
ValueError otherwise.

NOTE: Use a class decorator, not a function.

Examples:
    sum(2, 4, 6, 8)  # 20
    sum("a", "b", "c")  # ValueError
"""
import sys
from functools import wraps

class only_int_arguments(object):
    def __init__(self, original_function):
        wraps(original_function)(self)

    def __call__(self, *args):
        for arg in args:
            if type(arg) != int:
                raise ValueError 
        return self.__wrapped__(*args)

@only_int_arguments
def sum_integers(*args):
    return sum(list(args))

print (sum_integers(5, 2, 3))