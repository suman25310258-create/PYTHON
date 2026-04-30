#WAP TO FIND REMAINDER WITHOUT MODULO (%) OPERATOR
#-------------------------------------------------#

#Example 1:-Using Floor Division
#-------------------------------#
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
remainder = a - (a // b) * b
print("Remainder =", remainder)


#Example 2:-Using Repeated Subtraction
#------------------------------------#
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
temp = a
while temp >= b:
  temp -= b
print("Remainder =", temp)


#Example 3:-Using Recursion function
#-----------------------------------#
def remainder(a, b):
    if a < b:
        return a
    return remainder(a - b, b)

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

print("Remainder =", remainder(a, b))
