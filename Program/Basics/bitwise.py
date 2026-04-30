# DIFFERENT BITWISE OPERATOR

a=10 # a in Binary is = 01010, Left most bit is called sign bit.
b=5  # b in Binary is = 00101, Left most bit is called sign bit.
     # sign bit=0 for (+)ve number and 1 for (-)ve number
     
#Bitwise AND(&)
c=a&b
print("Result in Decimal:",c)
d=bin(a&b)
print("Result in Binary:",d)

print("")

#Bitwise OR(|)
c=a|b
print("Result in Decimal:",c)
d=bin(a|b)
print("Result in Binary:",d)

print(" ")

#Bitwise NOT(~)
c=~a
# a in binary is = 01010;
# Left-most 0 is for sign bit(+ve)
# So, ~a = ~01010 (~a = 1's complement of 'a')
#        =  10101 = -2**4 +2**2+2*0 = -11
print("Result in Decimal:",c)
d=bin(~a)
print("Result in Binary:",d)

print(" ")

#Bitwise XOR(^)
c=a^b
print("The Result in Decimal:",c)
d=bin(a^b)
print("The Result in Decimal:",d)