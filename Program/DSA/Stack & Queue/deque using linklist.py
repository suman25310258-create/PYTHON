# WAP TO DEMONSTRATE DOUBLE-ENDED-QUEUE (DEQUE) USING LINL-LIST
#-------------------------------------------------------------#
# A Deque allows insertion and deletion from both ends.
# We use a doubly linked list so we can move in both directions efficiently.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.data_count = 0
        

#================ Insert at front=======================
        
    def insert_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
            
        self.data_count+=1

#======================== Insert at rear ================
            
    def insert_rear(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
            
        self.data_count+=1    

#=================== Delete from front ==================
            
    def delete_front(self):
        if self.front is None:
            print("Deque is empty")
            return
        
        if self.front == self.rear:
            self.front = self.rear = None
             
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.data_count-=1  

#=================== Delete from rear ====================
            
    def delete_rear(self):
        if self.rear is None:
            print("Deque is empty")
            return
        
        if self.front == self.rear:
            self.front = self.rear = None
            
        else:
            self.rear = self.rear.prev
            self.rear.next = None
            
        self.data_count-=1  


#==================== Peek front ==========================
        
    def get_front(self):
        if self.front is None:
            return "Deque is empty"
        return self.front.data

#====================== Peek rear =========================
            
    def get_rear(self):
        if self.rear is None:
            return "Deque is empty"
        return self.rear.data
            
#====================== Size of Deque =====================
            
    def size(self):
        return self.data_count

#====================== Display Deque ====================
    
    def display(self):
       print("The Deque is :-")  
       if self.front is None:
         print("Deque is empty")
         return
    
       current = self.front   
       
       while current!= None:
         print(current.data, end=" <-> ")
         current = current.next
       print("None")
    
# ================= Driver Code ==========================

dq = Deque()

dq.insert_front(20)
dq.insert_front(10)
dq.insert_rear(30)
dq.insert_rear(40)
dq.insert_rear(50)

dq.display()

print("\nFRONT ELEMENT OF DEQUE IS:",dq.get_front())
print("REAR ELEMENT OF DEQUE IS:",dq.get_rear())
print("DEQUE SIZE IS:", dq.size())

dq.delete_front()
dq.delete_rear()
print("\nFRONT ELEMENT OF DEQUE IS:",dq.get_front())
print("REAR ELEMENT OF DEQUE IS:",dq.get_rear())
print("DEQUE SIZE IS:", dq.size())

dq.delete_front()
dq.delete_rear()
print("\nFRONT ELEMENT OF DEQUE IS:",dq.get_front())
print("REAR ELEMENT OF DEQUE IS:",dq.get_rear())
print("DEQUE SIZE IS:", dq.size())


dq.delete_front()
print("\nFRONT ELEMENT OF DEQUE IS:",dq.get_front())
print("REAR ELEMENT OF DEQUE IS:",dq.get_rear())
print("DEQUE SIZE IS:", dq.size())

