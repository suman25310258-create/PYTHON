# BREADTH-FIRST SEARCH (BFS) IN A BINARY TREE IS ALSO CALLED "LEVEL-ORDER-TRAVERSAL"
# IT VISITS NODES LEVEL BY LEVEL (left → right).
                      
#                             1
#                            / \
#                           2   3
#                          / \   \
#                         4   5   6
#==================================================================================

# USING "deque" A LIST-LIKE DATA STRUCTURE PROVIDED BY THE COLLECTION MODULE
#--------------------------------------------------------------------------#

from collections import deque

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def bfs(root):
  if not root:
    return

  queue = deque([root])

  while queue:
    current = queue.popleft()  # pop(0) in list is slow (O(n)), while popleft() in deque is fast (O(1)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

    print(current.data, end=" ")
  
    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)
            

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

bfs(root)            
            