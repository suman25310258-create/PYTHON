#WAP TO ACCESS(TRAVERSING) THE LIST ITEMS 

ls=[10,20,30,40,50,60]

#Method1:-Using Enumerate Method
for i,j in enumerate(ls):
#if you want to start from the index 1,then enmumerate(ls,start=1)
 print(i,"->",j)

print("\n")

#Method2:-Using range() and len() Method
for i in range(len(ls)):
#Can also be written as 'for i in range(len(ls[0:]))'    
 print(i,"has a value -->",ls[i])  
 
print("\n") 
 
#Method3:-Without using range() and len() method.
index = 0
for i in ls:
 print("Index", index, "has value -->", i)
 index += 1

print("\n")

#Method4:-Using while() loop
i=0
while i<len(ls):
 print(f"{i} has a value ---> {ls[i]}")
 i+=1
 