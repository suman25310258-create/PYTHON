#TRAVERSE A LINK-LIST AND INSERT NODE(START,END AND IN A SPECIFIC POSITION)#
#--------------------------------------------------------------------------#

class NODE:
 def __init__(self, data):
   self.data = data
   self.next = None
     
node1 = NODE(5)
node2 = NODE(6)
node3 = NODE(7)
node4 = NODE(8)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

#=============== TRAVERSE THE LINK-LIST==================

def print_Linklist(head):
  current = head
  while current != None:
    print(current.data, end="->")
    current = current.next
    
  print("NULL")
print_Linklist(head)

# ================= INSERT AT BEGINNING =================

def Insert_At_Beginning(head,data):
  newNode = NODE(data)
  newNode.next = head
  return newNode  # return newNode (with data 4) as new head.

head = Insert_At_Beginning(head,4) # update head with the value 4.
print_Linklist(head)

# ================= INSERT AT END =======================

def Insert_At_END(head,data):
    newNode = NODE(data)
    
    # Case 1: Empty list
    if head is None:
        return newNode
    
    # Case 2: Non-empty list
    current = head
    while current.next is not None:
      current = current.next
    current.next = newNode
    return head

head = Insert_At_END(head,9)
print_Linklist(head)

# =============== INSERT AT SPECIFIC POSITION ============

def Insert_At_Specific_Position(head,data,pos):
  newNode = NODE(data) # After position 7 (i.e; 50 at pos = 4)
  
  if pos == 0 or head is None:
    newNode.next = head
    return newNode

  current = head
  for i in range(pos-1):
     if current.next is None:
        break 
     current = current.next
   
  newNode.next = current.next
  current.next = newNode
  return head

head = Insert_At_Specific_Position(head,50,4)  
print_Linklist(head)

# ================= DELETE AT BEGINNING =================

def Delete_At_Beginning(head):
  if head is None:
    return None  
  head = head.next
  return head

head = Delete_At_Beginning(head)
print_Linklist(head)

# ================= DELETE AT END =======================

def Delete_At_End(head):
  # Case 1: Empty list
  if head is None:
    return None

  # Case 2: Only ONE node
  if head.next is None:
    return None
 
  # Case 3: More than ONE node
  current = head
  while current.next.next!= None:
    current = current.next
    
  current.next = None
  return head
head = Delete_At_End(head)
print_Linklist(head)

# ============== DELETE AT SPECIFIC POSITION ==============

def Delete_At_Specific_Position(head,pos):
  # Empty list
  if head is None:
     return None

  # Delete first node
  if pos == 0:
     return head.next

  current = head

  # Traverse to the node BEFORE the one to delete
  for i in range(pos - 1):
    if current.next is None:
       return head   # invalid position
    current = current.next  # Must be inside the for loop!

  # Delete the node
  if current.next is None:
    return head
  current.next = current.next.next
  return head

# Call the function
head = Delete_At_Specific_Position(head,3)
print_Linklist(head)
