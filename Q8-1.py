def quicksort_inplace(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_inplace(array, low, pivot_index - 1)
        quicksort_inplace(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1  
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

array = [10, 7, 8, 9, 11, 15,20, 1, 5,10, 7, 8, 9, 11, 15,20, 1, 5]
quicksort_inplace(array, 0, len(array) - 1)
print("Array ordenado:", array)