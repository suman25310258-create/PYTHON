# FACTORIAL OF A NUMBER USING RECURSION
#--------------------------------------#

def fact(a):
 if a==0:   # ✅ Base condition
  return 1
 else:
  return(a*fact(a-1))  # ✅ Recursion

num=int(input("Enter the Number : "))  
result=fact(num)

print("The factorial of the number is = ",result)