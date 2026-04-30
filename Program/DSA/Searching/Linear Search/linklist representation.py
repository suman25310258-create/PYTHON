# WAP OF LINK-LIST PRESENTATION OF LINEAR SEARCH
#----------------------------------------------#

class Node:
 def __init__(self, data):
   self.data = data
   self.next = None

# Create linked list manually
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Linear Search Function
def linear_search(head, key):
 current = head
 position = 0

 while current:
   if current.data == key:
      return position
   current = current.next
   position += 1

 return -1   # Not found

# Search value
print("Found at Position :",linear_search(head, 30))