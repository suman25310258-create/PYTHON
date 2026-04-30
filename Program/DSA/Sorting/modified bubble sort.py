# WAP TO DEMONSTRATE MODIFIED BUBBLE SORT IN ASCENDING ORDER
#----------------------------------------------------------#
def BubbleSort(arr): 
 for i in range(len(arr)):           # i for number of passes. After every pass,the largest element moves to the end.
   swapped = False                   # assume no swap 
   for j in range(0,len(arr)-i-1):   # j for comparing adjacent digits
     if arr[j] > arr[j+1]:
       arr[j], arr[j+1] = arr[j+1], arr[j]
       swapped = True                # mark swap is happened
     
   if not swapped:                   # stop if no swap (already sorted)
     break   

arr = [2, 3, 4, 9, 5]
print("The Unsorted List is :",arr)

BubbleSort(arr)
print("\nThe Sorted List in Ascending Order :",arr)