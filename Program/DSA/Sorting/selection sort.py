# WAP TO DEMONSTRATE SELECTION SORT IN ASCENDING ORDER
#----------------------------------------------------#
arr = [5, 3, 8, 4, 2]
print("Unsorted List is :",arr)

for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[j] < arr[min_index]:
      min_index = j    
  arr[i], arr[min_index] = arr[min_index], arr[i]

print("\nSorted List in Ascending Order :",arr)


# WAP TO DEMONSTRATE SELECTION SORT IN DESCENDING ORDER
#-----------------------------------------------------#
for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[j] > arr[min_index]:
      min_index = j 
  arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted List in Desending Order :",arr)