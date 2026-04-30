# DELATE A SPECIFIC NODE FROM THE END WITHOUT FINDING THE LENGTH (Two Pointer Approach))
#--------------------------------------------------------------------------------------#

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
node6 = Node(9)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Head node
head = node1


# Print linked list
def print_list(head):
  current = head
  while current:
    print(current.data, end=" -> ")
    current = current.next
  print("NULL")


print("Original Linked List:")
print_list(head)


# Delete N-th node from end (Two-pointer method)
def delete_specific_from_end(head, n):
  p1 = head
  p2 = head

  # Move p1 n steps ahead
  for _ in range(n):
     if p1 is None:
        return head
     p1 = p1.next
  
  # Handle head deletion
  if p1 == None:
    return head.next  

  # Move both pointers
  while p1.next!=None:
    p1 = p1.next
    p2 = p2.next

  # Delete the node
  p2.next = p2.next.next
  return head


# Delete 3rd node from end (i.e; 8)
head = delete_specific_from_end(head, 3)

print("\nLinked List after deletion:")
print_list(head)
