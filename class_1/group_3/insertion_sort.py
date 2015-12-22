#insertion sort

def insertion_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    for i in range (1, len(a_list)):
        j = i
        while j > 0 and a_list[j-1] > a_list[j]:
            temp = a_list[j-1]
            a_list[j-1] = a_list[j]
            a_list[j] = temp
            j = j-1
    return a_list
    
    
a_list = []
print (insertion_sort(a_list))