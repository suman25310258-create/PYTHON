# VARIOUS OPERATIONS ON DOUBLY LINKED LIST (INSERT, DELETION AT VARIOUS POSITION
#-------------------------------------------------------------------------------#
# Insert and deletion at specific position are done by searching the value.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
        
#=============== INSERT AT END ========================
        
    def insert_at_end(self, val):
       new_node = Node(val)
       
       # When the list is Empty
       if self.head is None:
         self.head = new_node 
         return

       current = self.head
       while (current.next != None):
          current = current.next

       current.next = new_node
       new_node.prev = current
       
# ================= INSERT AT BEGINNING ==================     

    def insert_at_beginning(self, val):
       new_node = Node(val)
       
       # When the list is Empty  
       if (self.head is None):
          self.head = new_node
          return
      
       new_node.next = self.head
       self.head.prev = new_node
       self.head = new_node
    
# =============== INSERT AT SPECIFIC POSITION ==============

    def Insert_At_Specific_position(self, val, x):
      new_node = Node(val)

      # If list empty
      if self.head is None:
        print("List is empty")
        return

      current = self.head

      # Search node with value x
      while current is not None:
        if current.val == x:
            break
        current = current.next

      # If value not found
      if current is None:
        print("Value not found")
        return

      # Insert node after x
      new_node.next = current.next
      new_node.prev = current

      if current.next is not None:
        current.next.prev = new_node

      current.next = new_node

      
#=============== TRAVERSE THE LINK-LIST===============
      
    def traversal(self):
      if self.head is None:
        print("Doubly Linklist is Emplty")
        return
    
      current = self.head
      while current is not None:
        print(current.val,end=" <-> ")
        current = current.next
      print("None")     
      
#=============== DELLETE AT THE BEGINNNG ==============
      
    def delete_at_beginning(self): 
       if self.head is None:
         print("List is empty")
         return
       
       # Move head to next node
       self.head = self.head.next
       
       # If list is not empty after deletion
       if self.head is not None:
         self.head.prev = None
      
#=============== DELLETE AT THE END ===================   
         
    def delete_at_end(self):        
       # Empty list
       if self.head is None:
         print("List is empty")
         return

       # Only one node
       if self.head.next is None:
         self.head = None
         return 
        
       # Traverse to last node 
       current = self.head  
       while (current.next is not None):
          current = current.next
          
       # deleting last node   
       current.prev.next = None
       
       
#================ DELETE AT THE MIDDLE ===================

    def delete_at_specific_position(self, x):
      # Empty list
      if self.head is None:
         print("List is empty")
         return

      current = self.head

      # Search node with value x
      while current is not None:
        if current.val == x:
           break
        current = current.next

      # Value not found
      if current is None:
        print("Value not found")
        return

      # If deleting first node
      if current.prev is None:
        self.delete_at_beginning()
        return

      # If deleting last node
      if current.next is None:
         self.delete_at_end()
         return

      # Delete middle node
      current.prev.next = current.next
      current.next.prev = current.prev
        
         
         
dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.traversal()

dll.insert_at_beginning(5)
dll.traversal()

# Insert 50 after 10
dll.Insert_At_Specific_position(50,10)
dll.traversal()

dll.delete_at_beginning()
dll.traversal()            

dll.delete_at_end()
dll.traversal()

dll.delete_at_specific_position(20)
dll.traversal()

    