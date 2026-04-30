# PRINT CLL / COUNT NUMBER OF NODES / MAX-MIN NODES / SEARCH INPUT NODES / IS CIRCULAR
#------------------------------------------------------------------------------------#

class NODE:
 def __init__(self, data):
   self.data = data
   self.next = None
     
node1 = NODE(5)
node2 = NODE(7)
node3 = NODE(4)
node4 = NODE(8)
node5 = NODE(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1   # Make it Circular

head = node1

#================= PRINT NODES AND COUNT NODES ========================

def print_Linklist():
  current = head
  count = 0
  while True:
     print(current.data, end=" -> ")
     current = current.next
     count+=1
     
     #For printing the last node
     if current == head:
       break            
   
  print("(Back to Head)")
  
  #Printing the number of nodes
  print("\nNumber of Nodes in this Circular Linked list is =",count)
  
print_Linklist() # Calling the function


#============================= MAX-MIN ================================

def find_max_min():
  current = head
  max_value = min_value = current.data

  while current.next != head:
    current = current.next

    if current.data > max_value:
        max_value = current.data

    if current.data < min_value:
       min_value = current.data

  print("\nMax:", max_value)
  print("Min:", min_value)
    
find_max_min()

# ======================= SEARCHING A NODE ============================

def search(node):
 if head is None:
   print("List is Empty")
   return
 current = head

 while True:
  if current.data == node:
    print("Item FOUND")
    break

  current = current.next

  if current == head:
    print("Not FOUND")
    break

num = int(input("\nEnter element to search: "))
search(num)  # Calling the search function


# ========================== IS CIRCULAR ===============================

def is_circular():
  if head is None:
    return False

  current = head.next
  while current is not None and current!= head:
    current = current.next

  if current == head:
     print("\nThe linked-list is Circular")
  else:
     print("The linked-list is NOT Circular")
     
is_circular()
