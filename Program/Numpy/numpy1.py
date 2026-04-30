#WAP TO DEMONSTRATE VARIOUS OPERATION ON NUMPY ARRAY
#--------------------------------------------------#

import numpy as np
print("THE VERSION OF THE NUMPY IS = ", np.__version__)

print("\n")

#Creating 0-D array
arr0=np.array(100)
print(f"This is a {arr0.ndim}-D Array")
print("Number of Element of this array is (size) =",arr0.size)
print(f"Array item is =",arr0)
print(f"Memory taken by this arry is = {arr0.nbytes} Bytes")
print(f"Single item size {arr0.itemsize} Bytes.")
print(f"Data-Type of the item is = {arr0.dtype}.")
print("The Shape of this Array is =", arr0.shape)  
print("The array object in this NumPy-Array is =", type(arr0)) 

print("\n")

#Creating 1-D array
arr1=np.array(["ram","sham","jadu","madhu","rahim"])
print(f"This is a {arr1.ndim}-D Array")
print("Number of Elements of this array are (size) =", arr1.size)
print(f"Array items are =",arr1)
print(f"Memory taken by this arry is = {arr1.nbytes} Bytes")
print(f"Single item size {arr1.itemsize} Bytes.")
print(f"Data-Type of the item is = {arr1.dtype}.")
print("The Shape of this Array is =", arr1.shape)  
print("The array object in this NumPy-Array is =", type(arr1))

print("\n")

#Creating 2-D array
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]]) #Number of items in both the sub-arry must be same
print(f"This is a {arr2.ndim}-D Array")
print("Number of Elements of this array are (size) =",arr2.size)
print("Array items are =")
print(arr2)
print(f"Memory taken by this arry is = {arr2.nbytes} Bytes")
print(f"Single item size {arr2.itemsize} Bytes.")
print(f"Data-Type of the item is = {arr2.dtype}.")
print("The Shape of this Array is =", arr2.shape)  # row=2,column=5
print("The array object in this NumPy-Array is =", type(arr2)) 

print("\n")

#Creating 3-D array
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]) #Number of items in both the sub-arry must be same
print(f"This is a {arr3.ndim}-D Array")
print("Number of Elements of this array are (size) =",arr3.size)
print("Array items are =")
print(arr3)
print(f"Memory taken by this arry is = {arr3.nbytes} Bytes")
print(f"Single item size {arr3.itemsize} Bytes.")
print(f"Data-Type of the item is = {arr3.dtype}.")
print("The Shape of this Array is =", arr3.shape)
print("The array object in this NumPy-Array is =", type(arr3)) 