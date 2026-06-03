# BREADTH-FIRST SEARCH (BFS) IN A BINARY TREE IS ALSO CALLED "LEVEL-ORDER-TRAVERSAL"
# IT VISITS NODES LEVEL BY LEVEL (left → right).
                      
#                             1
#                            / \
#                           2   3
#                          / \   \
#                         4   5   6
#----------------------------------------------------------------------------------

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def bfs(root):
 if not root:
   return
    
 queue = [root]   # simple list as queue
    
 while len(queue) > 0:       # can also write as --> "while queue != []:" OR  "while queue:"
   current = queue.pop(0)    # remove front
   print(current.data, end=" ")
        
   if current.left is not None:  # can also be written as --> "if current.left != None:"  OR  "if current.left:"
      queue.append(current.left)
   if current.right is not None: # can also be written as --> "if current.right != None:"  OR  "if current.right:"
      queue.append(current.right)
     
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

bfs(root)            
            