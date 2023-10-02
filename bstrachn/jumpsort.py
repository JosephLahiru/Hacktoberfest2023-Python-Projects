def jump_sort(arr):
    n = len(arr)
    jump = int(n**0.5)  # Jump distance

    # Perform jump sort
    for i in range(0, n, jump):
        # Find the insertion point for the current element
        key = arr[i]
        j = i - jump
        while j >= 0 and arr[j] > key:
            arr[j + jump] = arr[j]
            j -= jump
        arr[j + jump] = key

    # Perform final insertion sort on the sorted blocks
    for i in range(jump, n):
        key = arr[i]
        j = i - jump
        while j >= 0 and arr[j] > key:
            arr[j + jump] = arr[j]
            j -= jump
        arr[j + jump] = key

    return arr


# Example usage
arr = [29, 10, 14, 37, 13]
print("Original array:", arr)
sorted_arr = jump_sort(arr)
print("Sorted array:", sorted_arr)





