#WAP TO FIND A SPY NUMBER (EX-123,132,1124,1421...etc)
#EXAMPLE-1124
#PRODUCT=1*1*2*4=8
#SUM=1+1+2+4=8
#SUM=PRODUCT

n=int(input("Enter the number : "))
sum=0
product=1

while n>0:
 rem=n%10
 sum=sum+rem
 product=product*rem
 n=n//10

if(sum==product):
 print("This is a Spy Number")
else:
 print("This is not a Spy Number")

