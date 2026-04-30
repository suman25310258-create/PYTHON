#WAP TO ADD TWO GIVEN MATRICES

A=[[2,3,4],
   [1,2,3],
   [5,2,4]]

B=[[3,5,7],
   [5,6,7],
   [2,3,1]]

#Summation of two matrices
sum=[]
for i in range(len(A)):
 temp=[]   
 for j in range(len(B)):
    val=A[i][j]+B[i][j]
    temp.append(val)
 sum.append(temp)

#Print in proper matrix format
print("The sum of these two matrices:") 
for r in sum:
 print(r)    
   