#WAP TO FIND MAXIMUM SUM OF CONTIGUOUS SUB ARRAY IN PYTHON

def max_subarray_sum(arr):
 max_sum = arr[0]
 current_sum = arr[0]

 for i in range(1, len(arr)):
 # Either take current element alone or add to previous sum
   current_sum = max(arr[i], current_sum + arr[i])
   max_sum = max(max_sum, current_sum)

 return max_sum

# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(arr))
