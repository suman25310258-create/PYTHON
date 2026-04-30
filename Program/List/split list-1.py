#WAP TO SPLIT ALTERNATIVE ELEMENTS INTO TWO LISTS USING LOOP, LAST ELEMENT OF
#EACH LIST WILL BE THE SUM OF THE ALL ELEMENTS OF THAT LIST
 
Lst= [10,20,30,40,50,60]
Lst1=[]
Lst2=[]

for i in range(len(Lst)):
  if i%2==0:
    Lst1.append(Lst[i])
  else:
    Lst2.append(Lst[i])
    
Lst1.append(sum(Lst1))
Lst2.append(sum(Lst2))
print("1st List with altenative elements : ",Lst1)
print("2nd List with altenative elements : ",Lst2)

print("\n")

#SAME PROGRAM USING SLICING AND WITHOUT USING LOOP

lst1=Lst[::2]
lst2=Lst[1::2]

lst1.append(sum(lst1))
lst2.append(sum(lst2))

print("1st List with altenative elements : ",Lst1)
print("2nd List with altenative elements : ",Lst2)