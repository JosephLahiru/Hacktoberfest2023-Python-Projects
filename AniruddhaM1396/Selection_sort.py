def selection_sort(array):  
    # Looping through every element of the array  
    for i in range(len(array)):  
  
        # Searching the minimum element in the remaining subarray  
        min_ind = i  
        for j in range(i + 1, len(array)):  
            if array[min_ind] > array[j]:  
                min_ind = j  
  
        # Swaping the minimum element and the first element     
        array[i], array[min_ind] = array[min_ind], array[i]  
  
array = [23, 42, 3, 83, 36, 49, 19]  
   
selection_sort(array)  
  
print("The sorted array is: ")  
print(array) 