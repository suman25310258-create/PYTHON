#TRAVERSE A LINK-LIST AND INSERT & DELETE NODE(START,END AND IN A SPECIFIC POSITION)#
#-----------------------------------------------------------------------------------#

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

#============ TRAVERSE/PRINT THE LINK-LIST==================

def print_Linklist():
 current = head
 while current != None:
   print(current.data, end="->")
   current = current.next
 print("NULL")
print_Linklist()

#========== INSERT NEW NODE AT THE BEGINNING===============

newNode = NODE(4)
newNode.next = head
head = newNode
print_Linklist()

#========== INSERT NEW NODE AT THE END=====================

newNode = NODE(9)
current = head
while current.next != None:
 current = current.next
current.next = newNode
print_Linklist()

#===== INSERT NEW NODE AT THE SPECIFIC POSITION===========

pos=4  #between 7 and 8
newNode = NODE(50)
current = head
count=0

while current is not None and count < pos - 1:  #pos is 0-based index
# OR for i in range(pos-1):
 current = current.next
 count += 1
 
if current is None:
    print("Position out of range")
else: 
  newNode.next = current.next
  current.next = newNode
print_Linklist()


#=========== DELETE THE 1ST NODE OF THE LINK-LIST========

head = head.next  # move head to next node
print_Linklist()

#========= DELETE THE LAST NODE OF THE LINK-LIST==========

# If list is empty or only one node
if head is None or head.next is None:
  head = None
  
#If more than one node
else:
  current = head
  while current.next.next!= None:
    current = current.next
  current.next = None
print_Linklist()


#==========DELETE THE A SPECIFIC NODE (say 50)===========

pos=3
if head is None:
  print("List is empty")
  
#Delete first node and move head forward.  
elif pos == 0:
  head = head.next

#Traverse to (pos-1)th node to delete 50   
else:  
  current = head
  count=0
  while current is not None and count < pos - 1:
  #for i in range(pos-1):
    current = current.next
    count += 1
    
  #out-of-range check  
  if current is None or current.next is None:
    print("Position out of range")
  else:
      #Delete the node
      current.next = current.next.next 
print_Linklist()


