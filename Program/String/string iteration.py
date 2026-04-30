#WAP FOR VARIOUS STRING-ITERATION PROCESS

name="suman"
length=len(name)

#Iteration(simple)
for i in name:   
 print(i)
print("\n")

#Iteration using len() function and  range() 
for i in range(length): 
 print("name[",i,"]" , "->", name[i])
print("\n")

#Iteration with enumerate() function 
for i, j in enumerate(name):
 print(j) 