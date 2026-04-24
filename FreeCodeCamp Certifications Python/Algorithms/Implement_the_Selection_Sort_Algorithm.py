def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

unsorted_array = [29, 10, 14, 37, 13]
sorted_array = selection_sort(unsorted_array)

print("Sorted array:", sorted_array)