#WAP TO CREATE A DICTIONARY

n=int(input("How many key-value pair in your Dictionary : "))
d={}
for i in range(n):
 p=int(input("Enter the key : "))
 q=input("Enter the values : ")
 d.update({p:q})

print("My Dictionary is : ",d)  