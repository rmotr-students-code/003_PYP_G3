"""
Sorting Algorithms

Implement Bubble Sort(1) and Insertion Sort(2) algorithms:

    2: http://en.wikipedia.org/wiki/Insertion_sort
    1: http://en.wikipedia.org/wiki/Bubble_sort

"""
import random

def insertion_sort(my_list):
    for i in range(len(my_list)):
        j = i
        while j > 0 and my_list[j-1] > my_list[j]:
            #print j, my_list
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            j -= 1


def bubble_sort(my_list):
    n = len(my_list) 
    swapped = True
    while n > 0 and swapped:
        swapped = False
        for i in range(1, n):
            if my_list[i-1] > my_list[i]:
                swapped = True
                my_list[i-1], my_list[i] = my_list[i], my_list[i-1]



#for testing

def random_list(size=20, minimum=0, maximum=100):
    a = []
    for i in range(size):
        a.append(random.randrange(minimum,maximum))
    #a = random.sample(range(minimum,maximum), size)
    return a
    
my_list = random_list()
print("List to be sorted:\t\t" + str(my_list))
insertion_sort(my_list)
print("List after insertion_sort:\t" + str(my_list))
my_list = random_list()
print("List to be sorted:\t\t" + str(my_list))
bubble_sort(my_list)
print("List after bubble_sort:\t\t" + str(my_list))


