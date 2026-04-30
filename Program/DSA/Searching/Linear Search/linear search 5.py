# WAP TO SEARCH AN ELEMENT FROM THE LISTAND PRINT ITS POSITION
#------------------------------------------------------------#

Lst = [4, 8, 1, 9, 23, 64, 48, 50]
search = int(input("Enter the Element to search: "))

# Using inbuilt function 'index()'
if search in Lst:
  position = Lst.index(search)
  print(f"Element {search} found at position {position}:")
else:
  print(f"Element {search} not found in the list")