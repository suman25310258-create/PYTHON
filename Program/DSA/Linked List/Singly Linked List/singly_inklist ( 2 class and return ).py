# TRAVERSE A LINK-LIST AND INSERT & DELETE NODE(START,END AND IN A SPECIFIC POSITION)#
#------------------------------------------------------------------------------------#

class NODE:
   def __init__(self, data):
     self.data = data
     self.next = None
   
class SinglyLinklist:
   def __init__(self):
     self.head = None
     
# ================= INSERT AT END =======================

   def append(self,data):
      new_node = NODE(data)
      if self.head is None:  #when list is empty
         self.head = new_node
      else:
         current = self.head
         while current.next is not None:
           current = current.next
         current.next = new_node
          
# ================= INSERT AT BEGINNING =================

   def Insert_At_Beginning(self,data):
    newNode = NODE(data)
    newNode.next = self.head          
    self.head = newNode
  
  # =============== INSERT AT SPECIFIC POSITION ===========

   def Insert_At_Specific_Position(self,data,pos):
     newNode = NODE(data)
     
     # insert at beginning
     if pos == 0:
        self.Insert_At_Beginning(data)  # calling the same function which is already written
                 # OR
        # newNode.next = self.head
        # self.head = newNode
        return
    
     # checking negative position(index)
     if pos < 0:
       print("Invalid position")
       return
    
     current = self.head
     count = 0
     while current is not None and count < pos-1:
         current = current.next
         count+=1
     
     if current is None:
        print("Position out of range")
        return
        
     newNode.next = current.next
     current.next = newNode
        
 #=============== TRAVERSE THE LINK-LIST==================
     
   def traversal(self):
      if self.head is None:
        print("Singly Linklist is Emplty")
      else:
        current = self.head
        while current is not None:
          print(current.data,end=" -> ")
          current = current.next
        print("None")

# ================= DELETE AT BEGINNING =================

   def Delete_At_Beginning(self):
      if self.head is None:
          print("Singly Linked List is Empty")
      else:    
          self.head = self.head.next
          
# ================= DELETE AT END ========================

   def Delete_At_End(self):
      if self.head is None:
         print("Link-List is Empty")
         return
         
      if self.head.next is None:
        self.head = None   
        return
    
      current = self.head
      while current.next.next is not None:
         current = current.next
      current.next = None
      
# ============== DELETE AT SPECIFIC POSITION ==============      
 
   def Delete_At_Specific_Position(self, pos):
     if self.head is None:
        print("List-List is Empty")
        return

    # delete at beginning
     if pos == 0:
        self.Delete_At_Beginning()
               # OR
        #self.head = self.head.next
        return
    
     # checking negative position(index)
     if pos < 0:
       print("Invalid position")
       return

     current = self.head
     count = 0
     while current.next is not None and count < pos - 1:
        current = current.next
        count += 1

     if current.next is None:
        print("Position out of range")
        return

     current.next = current.next.next
    
    
SLL= SinglyLinklist()   

SLL.append(4)
SLL.append(5)
SLL.append(6)
SLL.append(7)
SLL.append(8)
SLL.traversal()

SLL.Insert_At_Beginning(3)
SLL.traversal()

# Insert value 50 at index no. 3
SLL.Insert_At_Specific_Position(50,3)
SLL.traversal()

SLL.Delete_At_Beginning()
SLL.traversal()

SLL.Delete_At_End()
SLL.traversal()

SLL.Delete_At_Specific_Position(2)
SLL.traversal()

# KEY RULE TO REMEMBER :-
 # Whenever you handle a special case (pos == 0, empty list, out-of-range), always return immediately.     