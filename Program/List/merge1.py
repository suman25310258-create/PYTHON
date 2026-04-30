#MERGE TWO LIST HAVE SAME/DIFFERENT LENGTH SUCH AS-
#Lst1=[1,2,3,4] AND Lst2=[10,20]
#MERGED LIST SHOULD BE: [1,10,2,20,3,4]


Lst1= list(map(int, input("Enter elements (comma-separated): ").split(',')))
Lst2= list(map(int, input("Enter elements (comma-separated): ").split(',')))

CLst=[]

#Checking the largest list
if len(Lst1)>len(Lst2):
  GL=Lst1
  SL=Lst2
else:
  GL=Lst2
  SL=Lst1
  
#Appending the items in main list  
for i in range(len(GL)):
  CLst.append(GL[i])
  if i<len(SL):
    CLst.append(SL[i])

#Printing the output
print(CLst)    