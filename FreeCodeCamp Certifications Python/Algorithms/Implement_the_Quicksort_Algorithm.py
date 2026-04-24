def quick_sort(array):
    if len(array) <= 1:
        return array
    
    # Choose the pivot from the last element of the list.
    pivot = array[-1]
    
    left_part = []
    right_part = []
    
    for i in range(len(array) - 1):
        if array[i] < pivot:
            left_part.append(array[i])  
        else:
            right_part.append(array[i]) 
            
    return quick_sort(left_part) + [pivot] + quick_sort(right_part)

random_number = [20, 2, 9, 7, 12, 15, 1, 6, 8]
result = quick_sort(random_number)

print("Sorted Numbers:", result)
