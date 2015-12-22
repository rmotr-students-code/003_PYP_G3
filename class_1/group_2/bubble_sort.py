a_list = [1, 16, 8, 14, 12, 9, 1]

def bubble_sort(a_list):
    i = 0
    list_is_sorted = False
    while i < len(a_list) - 1 and list_is_sorted == False:
        list_is_sorted = True
        j = 0
        for element in a_list[:-(i+1)]: 
            # a_list[:-(i+1)] decreases the for loop length for optimisation 
            # after each iteration
            if a_list[j] > a_list[j+1]:
                list_is_sorted = False
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j] 
            j+=1
        i+=1
    return a_list

    
print(bubble_sort(a_list))