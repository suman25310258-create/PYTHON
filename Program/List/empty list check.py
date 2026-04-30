#WAP TO CHECK WHETHER A LIST IS EMPTY OR NOT

mylist=[]

#Method 1:-Using boolean operation
if not mylist:
 print("The list is Empty.")
else: 
 print("The list is not Empty.")
 
#Method 2:- Using len() function
if len(mylist)==0:
 print("The list is Empty.")
else: 
 print("The list is not Empty.")
 
#Method 3:- Using indexing
if mylist==[]:
 print("The list is Empty.")
else: 
 print("The list is not Empty.") 
