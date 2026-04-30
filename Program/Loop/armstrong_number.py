# ARMSTRONG NUMBER => 153 = (1X1X1)+(5X5X5)+(3X3X3) = 153
#                  => 407 = (4X4X4)+(0X0X0)+(7X7X7) = 407
#                  => 1634 = (1x1x1x1)+(6X6x6x6)+(3x3x3x3)+(4x4x4x4) = 1634

num=int(input("Enter any Number : "))
order=len(str(num))

temp=num
sum=0

while temp>0:
 digit = temp%10
 sum=sum+digit**order
 temp=temp//10       #Floor division removes the last digit 
 
if sum==num:
 print("It is an Armstrong Number")
else:
 print("It is not an Armstrong Number")   
