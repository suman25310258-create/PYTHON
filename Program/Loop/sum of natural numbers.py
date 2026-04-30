#WAP TO CALCULATE THE SUM OF NATURAL NUMBERS USING FOR-LOOP
num=int(input("Enter the Number (>0) = "))

print("The sum of Natural Number upto", num, "is :-" )
sum=0
for i in range(1,num+1):
 print(i,end="+" if i!=num else "=") 
 sum=sum+i
print (sum)

print("\n")

#WAP TO CALCULATE THE SUM OF NATURAL NUMBERS USING WHILE-LOOP
p=int(input("Enter the Number (>0) = "))
n=p #store original value of p
sum=0
while(p>0):
 sum=sum+p
 p=p-1
print ("The sum of Natural Number upto",n,"is :",sum) 