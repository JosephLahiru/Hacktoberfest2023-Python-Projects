def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive call to merge_sort for both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from left and right subarrays and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add remaining elements from left and right subarrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
