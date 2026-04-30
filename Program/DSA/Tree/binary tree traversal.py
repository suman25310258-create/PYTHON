# TRAVERS THE FOLLOWING BINARY-TREE(PREORDER,INORDER,POSTORDER) /SEARCH/INSERT/DELETE
#                                      1
#                                    /   \
#                                   3     5
#                                  / \     \
#                                 2   4     8
# -------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ================================= TRAVERSAL =========================================

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

# ============================== SEARCH OF A SPECIFIC NODE =============================

def search(root, key):
    if root is None:
        return False  
    if root.data == key:
        return True   
    return search(root.left, key) or search(root.right, key)

# ============================== INSERTION OF A SPECIFIC NODE ===========================

def insert_left(root, target, value):
    if root is None:
        return False    
    # If target node found
    if root.data == target:
        root.left = Node(value)
        return True    
    # Search in left and right subtree
    return insert_left(root.left, target, value) or insert_left(root.right, target, value)


    
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

print("PREORDER TRAVERSAL OF NODES ARE: ", end=" ")  
preorder(root)

print("\nINORDER TRAVERSAL OF NODES ARE: ", end=" ")  
inorder(root)

print("\nPOSTORDER TRAVERSAL OF NODES ARE: ", end=" ")
postorder(root)


if search(root, 5):  # search for Node-5
    print("\nNODE 5 FOUND.")
else:
    print("\nNODE 5 NOT FOUND.")    

if search(root, 7):  # search for Node-7
    print("\nNODE 7 FOUND.")
else:
    print("NODE 7 NOT FOUND.")
    

insert_left(root, 5, 7)  # insert 7 to the left of 5
print("AFTER INSERTING 7 TO THE LEFT OF 5, THE PREORDER TRAVERSAL WILL BE:", end=" ")
preorder(root)

# ============================ DELETION OF A SPECIFIC NODE  ==============================

root.left.left = None  # remove 2 from the left of 3
print("\nAFTER DELETING 2 FROM LEFT OF 3, THE PREORDER TRAVERSAL WILL BE:", end=" ")
preorder(root)

def find_max(root):
    if root is None:
        return 0   
    
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    
    return max(root.data, left_max, right_max)
print("\nMAXIMUM VALUE IN TREE:", find_max(root))
    
    

         