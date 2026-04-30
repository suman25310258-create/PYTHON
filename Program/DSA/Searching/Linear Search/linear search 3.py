# WAP TO DEMONSTRATE LINEAR SEARCH  WITH USER INPUT AND 'WHILE' LOOP
#------------------------------------------------------------------#

def linear_search(arr, key):
  i = 0
  while i < len(arr):
    if arr[i] == key:
       return i
    i += 1
  return -1


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
  x = int(input("Enter element: "))
  arr.append(x)

key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result == -1:
  print("Element not found")
else:
  print("Element found at index", result)