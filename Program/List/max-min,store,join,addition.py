#WAP TO PERFORM THESE OPERATIONS--->JOIN/MAX-MIN/ADDITION OF TWO LIST.

#Input 1st List
n=int(input("How many numbers to enter in List1 : ")) 
lst1=[]
for i in range(n):
 x=int(input())
 lst1.append(x)
print("The List1 is :",lst1)

#Input 2nd List
n=int(input("How many numbers to enter in List2: ")) 
lst2=[]
for i in range(n):
 x=int(input())
 lst2.append(x)
print("The List2 is :",lst2)

#Joining 1st and 2nd List (Method:-1)
for x in lst2:
 lst1.append(x)
#print(lst1)

#Joining 1st and 2nd List (Method:-2)
#lst1.extend(lst2)
#print(lst1)

#Joining 1st and 2nd List (Method:-3)
#lst3=lst1+lst2
#print(lst3)

#Maximum & Minimum of the joining List
print("\nThe Joining List : ",lst1)
print("The Maximum Number of the Joining List: ",max(lst1+lst2))
print("The Minimum Number of the Joining List: ",min(lst1+lst2))

#Addition of Two List items
lst3=[]
for i in range(n):
 lst3.append(lst1[i]+lst2[i])
print("The Addition of two list is: ",lst3) 
