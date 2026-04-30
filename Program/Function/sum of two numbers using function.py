# WAP TO GET SUM OF 2 NUMBERS,AND FIND THE SUM IS EVEN/ODD USING FUNCTION

a=int(input("Enter 1st number = "))
b=int(input("Enter 2nd number = "))  

def operation ():
 sum=a+b
 return sum
    
p=operation()
print("The sum of these two Numbers is =",p)

if (p%2==0):
     print("The sum is an Even Number")
else :
 print("The sum is an Odd Number")  
