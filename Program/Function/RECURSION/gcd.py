# WAP TO FIND G.C.D OF TWO NUMBERS USING RECURSION
#------------------------------------------------#

def gcd(a, b):
 if b == 0:
   return a
 return gcd(b, a % b)

# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)

print("GCD is:", result)