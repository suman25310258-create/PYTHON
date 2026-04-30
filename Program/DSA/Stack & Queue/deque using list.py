# WAP TO DEMONSTRATE DOUBLE-ENDED-QUEUE (DEQUE) AND ITS BASIC OPERATIONS
#----------------------------------------------------------------------#
# A Deque allows insertion and deletion from both ends.

class Deque:
  def __init__(self):
     self.items = []
     
  def isEmpty(self):
      return len(self.items) == 0
    
  def Insert_At_End(self,value):
     self.items.append(value)
     
  def Delete_At_Front(self):
     if(self.isEmpty()):
       return "DEQUE IS EMPTY"
     else:
       return self.items.pop(0)
  
  def Insert_At_Front(self,value):
     self.items.insert(0,value)
     
  def Delete_At_End(self):
     if(self.isEmpty()):
        return "DEQUE IS EMPTY"
     else: 
        return self.items.pop()
      
DQ = Deque()

DQ.Insert_At_End(30)
DQ.Insert_At_Front(20)
DQ.Insert_At_End(40)
DQ.Insert_At_Front(10)
DQ.Insert_At_End(50)

print(DQ.Delete_At_End())
print(DQ.Delete_At_End())
print(DQ.Delete_At_Front())
print(DQ.Delete_At_Front())
print(DQ.Delete_At_Front())
print(DQ.Delete_At_Front())
print(DQ.Delete_At_End())