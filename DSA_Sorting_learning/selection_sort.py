#divides the array in sorted and unsorted regions
def selection_sort(arr):
    n = len(arr)
    # Traverse all array elements
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
numbers = [29, 10, 14, 37, 13]
print(selection_sort(numbers)) # Output: [10, 13, 14, 29, 37]
