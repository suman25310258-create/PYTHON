# WAP TO DEMONSTRATE BUBBLE SORT IN ASCENDING ORDER
#-------------------------------------------------#
def BubbleSort(arr): 
 for i in range(len(arr)):         # i for number of passes. After every pass,the largest element moves to the end.
  for j in range(0,len(arr)-i-1):  # j for comparing adjacent digits
   if arr[j] > arr[j+1]:
     arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 9, 1, 3]
print("The Unsorted List is :",arr)

BubbleSort(arr)
print("\nThe Sorted List in Ascending Order :",arr)


# WAP TO DEMONSTRATE BUBBLE SORT IN DESCENDING ORDER
#--------------------------------------------------#
def BubbleSort(arr):
 for i in range(len(arr)):  
  for j in range(0,len(arr)-i-1): 
   if arr[j] < arr[j+1]:   # change > to <
     arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 9, 1, 3]

BubbleSort(arr)
print("The Sorted List in Descending Order is :", arr)

# Why 'len(arr) - i - 1'  ?
# After each pass, the last elements are already sorted, so we don't need to check them again.