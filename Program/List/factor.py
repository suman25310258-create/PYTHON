#WAP TO CREATE A LIST OF FACTORS OF GIVEN NUMBER

num= int(input("Enter the number to get the factor(s) : "))
factor=[]
for i in range(1,num+1):
 if num%i==0:
   factor.append(i)
   
print(f"Factor of {num} is :",factor)   