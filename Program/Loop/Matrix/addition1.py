#WAP TO ADD TWO MATRICES OF ANY ORDER.INPUT TAKEN FROM THE USER.

row=int(input("How many rows : "))
col=int(input("How many coloumn : "))

#Input taken for the 1st matrix 
a=[]
for i in range(row):
 temp=[]
 for j in range(col):
   val=int(input(f"Enter values a[{i}][{j}] :"))
   temp.append(val)
 a.append(temp)

#Input taken for the 2nd matrix 
b=[]
for i in range(row):
 temp=[]
 for j in range(col):
   val=int(input(f"Enter values b[{i}][{j}] :"))
   temp.append(val)
 b.append(temp)

print("The Matrix a :",a)
print("The Matrix b :",b)

#Summation of two matrices
sum=[]
for i in range(row):
 temp=[]
 for j in range(col):
   val=a[i][j]+b[i][j]
   temp.append(val)
 sum.append(temp)
 print("The Sum of these 2 Matrix :",sum)

#Print in proper matrix format
print("The Sum of these 2 Matrix in proper format:")
for r in sum:
 print(r)  