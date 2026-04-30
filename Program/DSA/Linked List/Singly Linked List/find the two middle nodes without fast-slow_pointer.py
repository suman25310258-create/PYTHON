#FIND MIDDLE NODES OF A LINK-LIST FOR BOTH EVEN/ODD NUMBER OF NODES
#-----------------------------------------------------------------#

class Node:
 def __init__(self, data):
   self.data = data
   self.next = None

# CREATING NODES (Even numbers of nodes)
n1 = Node(5)
n2 = Node(7)
n3 = Node(4)
n4 = Node(10)
n5 = Node(9)
#n6 = Node(11)

# LINKING NODES
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
#n5.next = n6

#ASSIGNING 1st NODE INTO 'head' 
head = n1

#STEP-1:-COUNT LENGTH OF THE LINK-LIST
l = 0
current = head
while current:
  l += 1
  current = current.next

# FOR EVEN NUMBER OF NODES
if l%2 == 0: 
  #STEP-1: Find 1st Middle
  current = head
  for i in range((l // 2) - 1):
    current = current.next
  first_middle = current.data

  #STEP-2: Find 2nd Middle 
  second_middle = current.next.data
  print("Middle nodes are:",first_middle,  "and", second_middle)
  
# FOR ODD NUMBER OF NODES
if l%2 != 0:
  current = head
  for i in range(l // 2):
    current = current.next
  middle_node = current.data
  print("Middle node is:", middle_node)
