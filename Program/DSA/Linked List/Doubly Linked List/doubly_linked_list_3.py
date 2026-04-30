# VARIOUS OPERATIONS ON DOUBLY LINKED LIST (INSERT, DELETION AT VARIOUS POSITION
#-------------------------------------------------------------------------------#
# Insert and deletion at specific position are done by index of the value.
# Without edge-cases checking.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
#=============== INSERT AT END ==================================
        
    def insert_at_end(self, val):
       new_node = Node(val)
       
       # When the list is Empty
       if self.head is None:
         self.head = new_node 
         return

       current = self.head
       while current.next is not None:
          current = current.next

       current.next = new_node
       new_node.prev = current
       
#================= INSERT AT BEGINNING ========================     

    def insert_at_beginning(self, val):
       new_node = Node(val)
       
       # When the list is Empty  
       if (self.head is None):
          self.head = new_node
          return
      
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node
          
          
#=============== TRAVERSE THE LINK-LIST=========================
       
    def traversal(self):
      if self.head is None:
        print("Doubly Linklist is Emplty")
        return
      else:
        current = self.head
        while current is not None:
          print(current.val,end=" <-> ")
          current = current.next
        print("None")
      
                  
#=============== INSERT AT SPECIFIC POSITION ==================

    def Insert_At_Specific_position(self,val,pos):
     newNode = Node(val)
     
     # When the list is empty
     if self.head is None:
        print("List is empty")
        return
    
    
     current = self.head
     count = 0
     while current is not None and count < pos-1:
       current = current.next
       count+=1
     newNode.next = current.next
     current.next.prev = newNode
     newNode.prev = current
     current.next = newNode
     
     
#=============== DELETE AT BEGINNING =========================   
     
    def delete_at_beginning(self):
       
      # Case 1: empty list
      if self.head is None:
        print("List is empty")
        return

      # Case 2: only one node
      if self.head.next is None:
        self.head = None
        return

      # Case 3: multiple nodes
      self.head = self.head.next
      self.head.prev = None
      
#=============== DELETE AT END =============================
     
    def delete_at_end(self):

       #Case 1: Empty list
       if self.head is None:
         print("List is empty")
         return

       #Case 2: Only one node
       if self.head.next is None:
           self.head = None
           return

       #Case 3: More than one node
       current = self.head
       while current.next is not None:
         current = current.next
       current.prev.next = None
       
#=============== DELETE AT SPECIFIC POSITION ==================     
       
    def delete_at_specific_position(self, pos):

      # When the list is empty
      if self.head is None:
        print("List is empty")
        return

     
      current = self.head
      count = 0

      # Traverse to the required position
      while current is not None and count < pos:
        current = current.next
        count += 1

      current.prev.next = current.next
      current.next.prev = current.prev
   
             
dll = DoublyLinkedList()

dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_end(6)
dll.traversal()

dll.insert_at_beginning(1)
dll.traversal()

dll.Insert_At_Specific_position(10,2)
dll.traversal()

dll.delete_at_beginning()
dll.traversal()

dll.delete_at_end()
dll.traversal()

dll.delete_at_specific_position(2)
dll.traversal()
