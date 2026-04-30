#WAP TO ITERATE STRING IN REVERSE ORDER

name="SUMAN"
length=len(name)

#Iteration string in reverse order with (-)ve Slicing
for i in name[-1::-1]:   #can also be written as [::-1]
 print(i)
print("\n")

#Iteration string in reverse order using  range() function
for i in range(length-1,-1,-1):
 print(name[i])
print("\n")

#Iteration string in reverse order using reversed() function
for i in reversed(range(0,length)): #can also be written as range(length)
 print("name[",i,"]","=",name[i])  

                  