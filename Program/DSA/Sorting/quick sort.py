# WAP TO DEMONSTRATE QUICK SORT USING 'while()' LOOP
#--------------------------------------------------#
def quick_sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
  pivot = arr[low]  # FIRST element as pivot
  i = low + 1
  j = high

  while True:
    # move i right
    while i <= high and arr[i] <= pivot:
      i += 1
        
    # move j left
    while arr[j] > pivot:
       j -= 1
        
    if i < j:
       arr[i], arr[j] = arr[j], arr[i]
    else:
       break

  # place pivot in correct position
  arr[low], arr[j] = arr[j], arr[low]
  return j

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# WAP TO DEMONSTRATE QUICK SORT USING 'for()' LOOP
#-------------------------------------------------#
def quick_sort(arr, low, high):
 if low < high:
   pi = partition(arr, low, high)
   quick_sort(arr, low, pi - 1)
   quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
  pivot = arr[high]  # last element as pivot
  i = low - 1
    
  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# WAP TO DEMONSTRATE QUICK SORT USING 'append()' FUNCTION
#-------------------------------------------------------#
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # first element as pivot

    left = []
    right = []

    # partition using append()
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
   

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))


# WAP TO DEMONSTRATE QUICK SORT USING LIST COMPREHENSION
#-------------------------------------------------------#
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
    
  pivot = arr[0]  # choose first element as pivot
  left = [x for x in arr[1:] if x <= pivot]
  right = [x for x in arr[1:] if x > pivot]
    
  return quick_sort(left) + [pivot] + quick_sort(right)

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))