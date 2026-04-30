#SEARCH AN ELEMENT FROM THE LISTAND PRINT ITS POSITION

Lst = [4, 8, 1, 9, 23, 64, 48, 50]
search = int(input("Enter the Element to search: "))

#Method 1:- Using Flag with 'for' loop.
found = False
for i in range(len(Lst)):
  if Lst[i] == search:
    print("Element is found at position(index):",i)
    found = True
    break
 
if not found:
  print("Element not found")
 
#Method 2:- Using Flag 'index()' function
if search in Lst:
  position = Lst.index(search)
  print(f"Element {search} found at position {position}:")
else:
 print(f"Element {search} not found in the list")