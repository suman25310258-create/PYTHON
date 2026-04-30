# WAP ON CIRCULAR LNKED-LIST AND VARIOUS OPERATIONS ON IT (INSERT/DELETTE ETC.) #
#-------------------------------------------------------------------------------#

class Node:
  def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None


  
#================== IF LINKED IS EMPTY =====================
    
  def if_Empty(self,new_node):  
    self.head = new_node
    new_node.next = self.head
    
#================== INSERT AT END ========================== 
 
  def insert_at_end(self, data):
      
    new_node = Node(data)
    
    # If list is empty
    if self.head is None:
      self.if_Empty(new_node) # calling if_empty() function
      return
   
   # If list has at least one node
    current = self.head
    while current.next != self.head:
      current = current.next

    current.next = new_node
    new_node.next = self.head
    
#================== INSERT AT BEGINNING =====================

  def insert_begining(self, data):
      
    new_node = Node(data)

    # If list is empty
    if self.head is None:
       self.if_Empty(new_node)
       return
  
    current = self.head

    # Go to last node
    while current.next != self.head:
      current = current.next

    # Link new node
    new_node.next = self.head
    current.next = new_node
    self.head = new_node

#================== INSERT AT SPECIFIC POSITION ================
    
  def insert_at_position(self, data, pos):
      
    new_node = Node(data)

    # Invalid position
    if pos < 0:
        print("Position out of range")
        return

    # If list is empty
    if self.head is None:
        if pos == 0:
            self.if_Empty(new_node)
        else:
            print("Position out of range")
        return

    # Insert at beginning
    if pos == 0:
        self.insert_begining(data)
        return

    current = self.head
    count = 0

    while count < pos - 1 and current.next != self.head:
        current = current.next
        count += 1

    if count != pos - 1:
        print("Position out of range")
        return

    new_node.next = current.next
    current.next = new_node
    
#================= TRAVERSAL/DISPLAY THE LINKEDLIST ===============
    
  def display(self):
    if self.head is None:
        print("List is empty")
        return

    current = self.head

    while current.next != self.head:
        print(current.data, end=" -> ")
        current = current.next

    # Print last node
    print(current.data, end=" -> ")
    print("(Back to Head)")
    
#======================== DELETE AT BEGINING =======================
    
  def delete_at_beginning(self):
      
    # If list is empty
    if self.head is None:
        print("List is empty")
        return

    # If only one node
    if self.head.next == self.head:
        self.head = None
        return
    
    # Go to last node
    current = self.head
    while current.next != self.head:
      current = current.next
    current.next = self.head.next
    self.head = self.head.next
    
#======================== DELETE AT END =======================
    
  def delete_at_end(self):
      
    # If list is empty
    if self.head is None:
        print("List is empty")
        return

    # If only one node
    if self.head.next == self.head:
        self.head = None
        return
    
    # Go to 2nd last node
    current = self.head
    while current.next.next != self.head:
      current = current.next
    current.next = self.head
    
#=================== DELETE AT SPECIFIC POSITIONN ==================  
      
  def delete_at_specific_position(self, pos):
    
    # Empty posiion
    if self.head is None:
        print("List is empty")
        return
    
    # Negative positionn(index)
    if pos < 0:
        print("Position out of range")
        return

    # Delete beginning
    if pos == 0:
        self.delete_at_beginning()
        return

    current = self.head
    count = 0
    
    # Move to node before the position
    while count < pos - 1 and current.next != self.head:
        current = current.next
        count += 1
        
     # If position is invalid
    if count != pos - 1 or current.next == self.head:
        print("Position out of range")
        return
    
    current.next = current.next.next
    
     

CLL = CircularLinkedList()

CLL.insert_at_end(10)
CLL.insert_at_end(20)
CLL.insert_at_end(30)
CLL.insert_at_end(40)
CLL.insert_at_end(50)
CLL.display()

CLL.insert_begining(5)
CLL.display()

CLL.insert_at_position(35,4)
CLL.display()

CLL.delete_at_beginning()
CLL.display()

CLL.delete_at_end()
CLL.display()

CLL.delete_at_specific_position(3)
CLL.display()