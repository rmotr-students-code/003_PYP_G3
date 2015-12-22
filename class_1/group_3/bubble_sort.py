#bubble sort

def bubble_sort(values):
    length = len(values) - 1
    if len(values) <= 1:
        return values
    for j in range (0,length):
        for i in range (0,length):
            if values[i] > values[i + 1]:
                temp = values[i+1]
                values[i+1] = values[i]
                values[i] = temp
    return values
    
    
values = [7]    
print(bubble_sort(values))