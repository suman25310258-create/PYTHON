# WAP TO DEMONSTRATE LINK-LIST VERSION OF BINARY SEARCH 
#------------------------------------------------------#

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


# Creating list: 1 → 3 → 5 → 7 → 9
head=Node(1)
head.next=Node(3)
head.next.next=Node(5)
head.next.next.next=Node(7)
head.next.next.next.next=Node(9)

print(binary_search(head,7))