# WAP ON CIRCULAR LNKED-LIST AND VARIOUS OPERATIONS ON IT (INSERT/DELETTE ETC.) #
#-------------------------------------------------------------------------------#
# Program is without edge-case checking.

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
     
     if self.head is None:
        self.if_Empty(new_node)
        return
     
     current = self.head
     while current.next != self.head:
       current = current.next

     current.next = new_node
     new_node.next = self.head
    
#================== INSERT AT BEGINNING =====================

  def insert_begining(self, data):
      
    new_node = Node(data)    
    
    current = self.head
    while current.next != self.head:
      current = current.next

    new_node.next = self.head
    current.next = new_node
    self.head = new_node

#================== INSERT AT SPECIFIC POSITION ================
    
  def insert_at_position(self, data, pos):
      
    new_node = Node(data)

    current = self.head
    count = 0

    while count < pos - 1 and current.next != self.head:
        current = current.next
        count += 1

    new_node.next = current.next
    current.next = new_node
    
#================= TRAVERSAL/DISPLAY THE LINKEDLIST ===============
    
  def display(self):
    
    current = self.head
    while current.next != self.head:
        print(current.data, end=" -> ")
        current = current.next

    print(current.data, end=" -> ")
    print("(Back to Head)")
    
#======================== DELETE AT BEGINING =======================
    
  def delete_at_beginning(self):
      
    current = self.head
    while current.next != self.head:
      current = current.next
    current.next = self.head.next
    self.head = self.head.next
    
#======================== DELETE AT END =======================
    
  def delete_at_end(self):
      
    current = self.head
    while current.next.next != self.head:
      current = current.next
    current.next = self.head
    
#=================== DELETE AT SPECIFIC POSITIONN ===============
      
  def delete_at_specific_position(self, pos):
   
    current = self.head
    count = 0
    
    # Move to node before the position
    while count < pos - 1 and current.next != self.head:
        current = current.next
        count += 1
    current.next = current.next.next
    
#=================== FUNCTION CALL ==============================      

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