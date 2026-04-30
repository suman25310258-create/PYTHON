# WAP OF RECURSIVE VERSION OF LINEAR SEARCH
#-----------------------------------------#

def linear_search(arr, x, i=0):
  if i == len(arr):      # base case: reached end
     return -1
  if arr[i] == x:       # element found
     return i
  return linear_search(arr, x, i+1)   # recursive call


arr = list(map(int, input("Enter elements (space separeted): ").split()))
x = int(input("Enter element to search: "))

result = linear_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")