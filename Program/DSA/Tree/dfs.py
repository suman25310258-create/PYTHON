# DEPTH-FIRST SEARCH (DFS) IN BINARY-TREE(PREORDER,INORDER,POSTORDER)
#                                      1
#                                     / \
#                                    3   5
#                                   / \   \
#                                  2   4   8
# ------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ================================= TRAVERSAL ========================================

def preorder(root):     # Order : Root → Left → Right
   if(root!= None):
       print(root.data, end=" ")
       preorder(root.left)
       preorder(root.right)       
     
def inorder(root):      # Order : Left → Root → Right
   if(root!= None):
       inorder(root.left)
       print(root.data, end=" ")
       inorder(root.right)

def postorder(root):    # Order : Left → Right → Root  
   if(root!= None):
       postorder(root.left)
       postorder(root.right)
       print(root.data, end=" ")
       

root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("PREORDER TRAVERSAL OF NODES ARE : ", end=" ")  
preorder(root)

print("\nINORDER TRAVERSAL OF NODES ARE : ", end=" ")  
inorder(root)

print("\nPOSTORDER TRAVERSAL OF NODES ARE : ", end=" ")
postorder(root)


