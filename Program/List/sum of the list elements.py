#WAP TO FIND THE SUM OF THE LIST ELEMENTS 

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#sum using range() and len() functions
s=0
for i in range(len(List)):
 s=s+List[i]
print(s) 

#sum using index numbers
s=0
for i in List[0:]:
 s=s+i
print(s)

#sum using sum() function
print(sum(List))

#sum using list-compression technique(Method-1)
print(sum([i for i in List]))

#sum using list-compression technique(Method-2)
print(sum([i for i in range(len(List)+1)]))

#sum using 'while' loop
s=0
i=0
while (i<(len(List))):
 s=s+List[i]
 i=i+1
print(s) 
 


  