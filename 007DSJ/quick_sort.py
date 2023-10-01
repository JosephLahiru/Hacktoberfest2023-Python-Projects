def swap(arr, index1 , index2):
  temp=arr[index1]
  arr[index1]=arr[index2]
  arr[index2]=temp


def pivot(arr, pivot_index , end_index):
  swap_index=pivot_index
  for i in range(pivot_index+1,end_index+1):
    if arr[i] < arr[pivot_index]:
      swap_index+=1
      swap(arr,swap_index,i)
  swap(arr,pivot_index,swap_index)
  return swap_index

def quick_sort(arr,left,right):
  if left < right:
    pivot_index=pivot(arr,left,right)
    quick_sort(arr,left,pivot_index)
    quick_sort(arr,pivot_index+1,right)
  return arr
  
arr=[1,2,6,87,9,45]
print(arr)

arr=quick_sort(arr,0,len(arr)-1)

print(arr)
