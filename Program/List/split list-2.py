#WAP TO SPLIT ALTERNATIVE ELEMENTS INTO TWO LISTS USING LOOP, LAST ELEMENT OF
#EACH LIST WILL BE THE SUM OF THE ALL ELEMENTS OF THAT LIST

Lst= list(map(int, input("Enter elements (comma-separated): ").split(',')))

print("Original List is : ",Lst)

Lst1=[]
Lst2=[]

S1=S2=0
for i in range(len(Lst)):
  if i%2==0:
    Lst1.append(Lst[i])
    S1=S1+Lst[i]
  else:
    Lst2.append(Lst[i])
    S2=S2+Lst[i]
   
Lst1.append(S1)
Lst2.append(S2)

print("1st List with alternative elements : ",Lst1)
print("2nd List with alternative elements : ",Lst2)
