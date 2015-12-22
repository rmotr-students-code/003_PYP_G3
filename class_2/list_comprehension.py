# divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)  # [9, 6, 3]

"""
def divisible_numbers(a_list, term):
    return [x for x in a_list if x%term == 0]
    
print divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
"""

def is_divisible_by_all_terms(elem, terms):
    # True, False
    return len(terms) == len([elem for term in terms if elem % term == 0])


assert is_divisible_by_all_terms(4, [2]) is True, is_divisible_by_all_terms(4, [2])
assert is_divisible_by_all_terms(8, [4, 2]) is True
assert is_divisible_by_all_terms(8, [3]) is False
assert is_divisible_by_all_terms(8, [4, 3]) is False

def divisible_numbers(a_list, terms):
    return [x for x in a_list if len(terms) == len([x for term in terms if x % term == 0])]


assert divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3]) ==  [12, 6]


"""
elem = 8
terms = [4, 2]

res1 = [elem for term in terms if elem % term == 0]
print(res1)
"""


