#WAP TO VERIOUS OPERATION WITH LIST ITEMS

list=[0,1,2,3,4,5,6,7,8,9]

#Through loop
for i in list:
 print(i)
 
print("\n")    

#Through Loop Comprehension
newlst= [i for i in list]
print(newlst)

print("\n")

#Print first 5 number of the list by 'List-Comprehension' and 'range()'
m=[i for i in range(5)]
print(m)

print("\n")

#Find Even number by using Loop,range() and 'append()' function
newlist=[]
for i in list:
 if i%2==0:
  newlist.append(i)
print(newlist)

print("\n")

#Find Even number by Loop Comprehension,range() with condition (one-liner)
newlist=[i for i in range(10) if i%2==0]
print(newlist)