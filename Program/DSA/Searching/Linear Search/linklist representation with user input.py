# WAP OF LINK-LIST PRESENTATION OF LINEAR SEARCH WITH USER INPUT
#--------------------------------------------------------------#

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def linear_search(head, key):
  current = head
  position = 0

  while current:
    if current.data == key:
       return position
    current = current.next
    position += 1

  return -1


# Create linked list using user input
n = int(input("Enter number of nodes: "))

head = None
temp = None

for i in range(n):
  x = int(input("Enter data: "))
  new = Node(x)

  if head == None:
     head = new
     temp = new
  else:
     temp.next = new
     temp = new


key = int(input("Enter element to search: "))

pos = linear_search(head, key)

if pos == -1:
    print("Element not found")
else:
    print("Found at Position:", pos)