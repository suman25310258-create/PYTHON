# WAP TO DEMONSTRATE BINARY SEARCH WITH RECURSION AND USER INPUTS
#---------------------------------------------------------------#

def binary_search(arr, low, high, key):
  if low > high:
     return -1

  mid = (low + high) // 2

  if arr[mid] == key:
     return mid
  elif arr[mid] < key:
     return binary_search(arr, mid + 1, high, key)
  else:
     return binary_search(arr, low, mid - 1, key)



arr=list(map(int,input("Enter sorted elements (space separeted): ").split()))
key=int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
 print("Element found at index", result)
else:
 print("Element not found")