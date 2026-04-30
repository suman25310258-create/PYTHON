# WAP TO DEMONSTRATE INSERTION SORT IN ASCENDING ORDER
#----------------------------------------------------#
def insertion_sort_ascen(arr):
 for i in range(1, len(arr)):
   key = arr[i]
   j = i - 1
        
   while j >= 0 and arr[j] > key:
     arr[j+1] = arr[j]
     j = j - 1
            
   arr[j+1] = key

arr = [5, 2, 9, 1, 6]
insertion_sort_ascen(arr)
print("Sorted List in Ascending Order :",arr)


# WAP TO DEMONSTRATE INSERTION SORT IN DESCENDING ORDER
#-----------------------------------------------------#
def insertion_sort_desc(arr):
 for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
        
    while j >= 0 and arr[j] < key:
      arr[j + 1] = arr[j]
      j -= 1
            
    arr[j + 1] = key

arr = [5, 2, 9, 1, 6]
insertion_sort_desc(arr)
print("Sorted List in Descending Order :",arr)