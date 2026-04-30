# SEARCH AN ELEMENT FROM THE LIST AND PRINT ITS POSITION
# -----------------------------------------------------#

Lst = [4, 8, 1, 9, 23, 64, 48, 50]
search = int(input("Enter the Element to search: "))

for i in range(len(Lst)):
  if Lst[i] == search:
    print("Element is found at position(index):",i)
    break
else:  
   print("Element is not found")
   
 
