def insertion_sort(a_list):

    for elem in a_list[1:]:
        i = a_list.index(elem)
        
        while i > 0 and a_list[i - 1] > elem:
            a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
            i -= 1
    return a_list
            
a_list = [6, 4, 12, 8, 3, 2]
print insertion_sort(a_list)