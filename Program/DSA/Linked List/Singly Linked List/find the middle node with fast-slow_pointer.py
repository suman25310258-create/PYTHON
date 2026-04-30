#FIND MIDDLE NODE OF A LINKED NODES (USING 'FAST-SLOW' POINTER)#
#--------------------------------------------------------------#

# Node class
class Node:
 def __init__(self, data):
   self.data = data
   self.next = None

# Creating nodes
n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)
n5 = Node(9)

# Linking nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Head of the linked list
head = n1

# Function to find middle (Slow-Fast Pointer)
def find_middle(head):
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  print("Middle node is:",slow.data)
  
# Calling function
find_middle(head)