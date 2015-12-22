
my_list = [2, 4, 18, 2, 7, 12, 11, 2]

def is_even(x):
    return x % 2 == 0
    
def takeWhile(input_list, condition):
    output = []
    for i in input_list:
        if not condition(i):
            return output
        output.append(i)
    return output

result = takeWhile(my_list, lambda x: x % 2 == 0)
assert result == [2, 4, 18, 2], "The result returned {} is not what I was expecting".format(result)

"""
def print_report(format, verbosity):
    pass

options = {
    'format': '%Y-%m',
    'verbosity': 2
}

print(my_sum(**options))
"""

lambda x: x % 2 == 0 and x < 20 and 