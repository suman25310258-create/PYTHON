# WAP TO DEMONSTRATE LINK-LIST VERSION OF BINARY SEARCH WITH USER INPUT
#----------------------------------------------------------------------#

class Node:
 def __init__(self,data):
   self.data=data
   self.next=None

def middle(start,last):
  slow=start
  fast=start
    
  while fast!=last and fast.next!=last:
    fast=fast.next.next
    slow=slow.next
        
  return slow

def binary_search(head,key):
  start=head
  last=None
    
  while start!=last:
    mid=middle(start,last)
        
    if mid.data==key:
       return "Found"
    elif mid.data < key:
       start=mid.next
    else:
       last=mid
            
  return "Not Found"


# Create Linked List using user input
n=int(input("Enter number of nodes: "))

head=None
temp=None

for i in range(n):
  x=int(input("Enter data: "))
  new=Node(x)

  if head==None:
    head=new
    temp=new
  else:
    temp.next=new
    temp=new

key=int(input("Enter element to search: "))

print(binary_search(head,key))