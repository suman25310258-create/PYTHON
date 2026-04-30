# DELATE A SPECIFIC NODE WHEN 'HEAD' IS NOT GIVEN (should not be the last node)
#------------------------------------------------------------------------------#

class NODE:
 def __init__(self, data):
   self.data = data
   self.next = None
     
node1 = NODE(5)
node2 = NODE(6)
node3 = NODE(1)
node4 = NODE(8)
node5 = NODE(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# PRINT THE LINK-LIST
print("Before Deletion:")
def print_Linklist(head):
 current = head
 while current != None:   
   print(current.data, end="->")
   current = current.next
 print("NULL")
print_Linklist(head)

# DELETE THE node3(i.e; 1) FROM LINK-LIST
def Delete_At_Specific_Position(node):
 if node is None or node.next is None:
   print("Cannot delete last node using this method")
   return   
 node.data = node.next.data # Equallying the 'node4' and 'node3' value.
 node.next = node.next.next
Delete_At_Specific_Position(node3)

print("\nAfter deletion:")
print_Linklist(head)