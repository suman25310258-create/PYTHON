# DELATE A SPECIFIC NODE FROM THE END (should not be the last node)
#------------------------------------------------------------------#

# Node class
class Node:
 def __init__(self, data):
   self.data = data
   self.next = None

# Creating nodes
node1 = Node(5)
node2 = Node(6)
node3 = Node(1)
node4 = Node(8)
node5 = Node(3)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Head node
head = node1

# PRINT THE ORIGINAL LINKED LIST
def print_list(head):
 current = head
 while current:
   print(current.data, end=" -> ")
   current = current.next
 print("NULL")

print("Original Linked List:")
print_list(head)

# DELETE SPECIFIC NODE (say 8 , i.e; 2nd node from behind)
def delete_specific_from_end(n):
# Step 1: Count nodes
 length = 0
 current = head
 while current is not None:
   length += 1
   current = current.next

# Step 2: Go to (length - (n + 1))th node (i.e; previous node of 8)
 current = head
 for i in range(length - (n + 1)):
   current = current.next

# Step 3: Delete node
 current.next = current.next.next

delete_specific_from_end(n=2) 

print("\nLinked List after deletion:")
print_list(head)
