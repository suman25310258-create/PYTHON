#WAP TO ACCESS ROWS,COLUMNS,INDIVIDUAL ITEMS OF NUMPY ARRAY (2D)
#--------------------------------------------------------------#
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

row1 = arr[0]     # First row
row2 = arr[1]     # Second row
row3 = arr[2]     # Third row

print("2nd Row is =",row2)
print("\n")

rows = arr[[0, 2]]   # Access row 0 and row 2
print("Row-1 and Row-2 are :- \n",rows)
print("\n")

first_two_rows = arr[0:2]
print("First Two Rows are :- \n", first_two_rows)
print("\n")

value = arr[1][2]    # row index 1, column index 2
# or
value = arr[1, 2]
print("Value at ROW-1 and Column-2 is =>" ,value)  # Output: 60
print("\n")

print("1st Column => ", arr[:, 0])  # 1st column
print("2nd Column => ", arr[:, 1])  # 2nd column
print("3rd Column => ", arr[:, 2])  # 3rd column
print("\n")

print("1st Column in 2D format => ")
print(arr[:, 0:1])
print("\n")

print("2nd Column in 2D format => ")
print(arr[:, 1:2])
print("\n")

print("3rd Column in 2D format => ")
print(arr[:, 2:3])
print("\n")

print("Extract first 2 Rows => ")
print(arr[0:2, :])
print("\n")

print("Extract first 2 Columns => ")
print(arr[:, 0:2])
print("\n")

print("Extract middle 2x2 block => ")
print(arr[0:2, 1:3])
print("\n")

print("Print Diagonal Elements => ")
print(np.diag(arr))
print("\n")

print("Print Reverse Rows => ")
print(arr[::-1])
print("\n")

print("Print Reverse Columns => ")
print(arr[:, ::-1])
print("\n")

print("Print Items which are > 50 => ")  #Boolean Indexing
print(arr[arr > 50])