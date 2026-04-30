#WAP TO MERGE MULTIPLE DICTIONARIES INTO ONE

n1=int(input("How many key-value pair in 1st Dictionary : "))
d1={}
for i in range(n1):
 p=input("Enter the key   : ")
 q=input("Enter the values: ")
 d1.update({p:q}) 
print("The 1st Dictionary is : ",d1)

n2=int(input("How many key-value pair in 2nd Dictionary : "))
d2={}
for i in range(n2):
 x=input("Enter the key : ")
 y=input("Enter the values : ")
 d2.update({x:y})
print("The 2nd Dictionary is : ",d2)

n3=int(input("How many key-value pair in 3rd Dictionary : "))
d3={}
for i in range(n3):
 k=input("Enter the key : ")
 v=input("Enter the values : ")
 d3.update({k:v})
print("The 3rd Dictionary is : ",d3)

d1.update(d2) #update() method takes only 1 argument at a time.So can't write as- d1.update(d2,d3)
d1.update(d3) 

print("The combined Dictionary : ",d1)