# WAP TO DEMONSTRATE BINARY SEARCH WITH THE HELP OF 'FOR' LOOP
#------------------------------------------------------------#

def binary_search(arr, key):
  low = 0
  high = len(arr) - 1

  for i in range(len(arr)):   # maximum possible iterations
    if low > high:
       break
    
    mid = (low + high) // 2

    if arr[mid] == key:
      return mid    
    elif arr[mid] < key:
       low = mid + 1       
    else:
      high = mid - 1

  return -1


arr = [2, 4, 6, 8, 10, 12]
key = 8

result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")