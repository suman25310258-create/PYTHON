#SUM OF TWO NUMBERS, AND FIND WHICH ONE IS LARGER

x=int(input("Enter 1st Integer:"))
y=int(input("Enter 2nd Integer:"))
z=x+y
print ("The Sum of",x,"and",y, "is :",z)

if(x>y):
 print(x,"is larger than",y)
else:
 print(y,"larger than",x)