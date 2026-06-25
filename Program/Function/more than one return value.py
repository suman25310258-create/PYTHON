#EXAMPLE OF MORE THAN ONE RETURN VALUE
#------------------------------------#

def calculator (x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    
    return a,b,c,d

sum,sub,mul,div = calculator(6,4)

print("THE VALUE OF THE SUMMATION      :",sum)
print("THE VALUE OF THE DEDUCTION      :",sub)
print("THE VALUE OF THE MULTIPLICATION :",mul)
print("THE VALUE OF THE DIVISION       :",div)