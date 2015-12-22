# [1, 2, 3] > [2, 4, 6]

#[user1, user2, user3] > [u1@gmail.com, u2@gmail.com, u3@gmail.com]

a_list = [1, 2, 3]

"""
result = map(lambda x: x, a_list)
print(result)

result2 = [x for x in a_list]
print(result2)
"""

# [1, 2, 3] > [2, 4, 6]
"""
def double(x):
    return x * 2

doubles = []
for elem in a_list:
    doubles.append(double(elem))

doubles = map(lambda x: x * 2, a_list)

doubles = [elem * 2 for elem in a_list]

print(doubles)

"""

"""
# Map:
# [1, 2, 3] > [2, 4, 6]

# Filter
# [1, 2, 3] > [1, 2]
# [1, 2, 3, 4] > [2, 4]

a_list = [1, 2, 3]

filter(lambda x: x < 3, a_list)
[elem for elem a_list if elem < 3]


less_than_3 = []
for elem in a_list:
    if elem < 3:
        less_than_3.append(elem)
less_than_3 == [1, 2]


"""

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


res = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))
print res

print [x * 2 for x in numbers if x % 2 == 0]
"""

# Map:
# [1, 2, 3] > [2, 4, 6]

# Filter:
# [1, 2, 3] > [1, 2]

# Reduce:
# [1, 7, 2, 3] > 7

numbers = [1, 2, 3, 4]

"""
acc = 0
for elem in numbers:
    acc += elem
print(acc)
"""






