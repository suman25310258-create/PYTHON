# WAP TO DEMONSTRATE VARIOUS OPERATION ON "SINGLY LINKED-LIST" WITH "MENU-DRIVEN" FORMAT
#=======================================================================================#

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
    
# ==================== MENU =========================

SLL = SinglyLinklist()

while True:
    print("=========== MENU =============")
    print("1. Insert at End")
    print("2. Insert at Beginning")
    print("3. Insert at Specific Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Delete at Specific Position")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        SLL.append(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        SLL.Insert_At_Beginning(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        SLL.Insert_At_Specific_Position(value,pos)

    elif choice == 4:
        SLL.Delete_At_Beginning()

    elif choice == 5:
        SLL.Delete_At_End()

    elif choice == 6:
        pos = int(input("Enter position: "))
        SLL.Delete_At_Specific_Position(pos)

    elif choice == 7:
        SLL.traversal()

    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")