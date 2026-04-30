# ARMSTRONG NUMBER  WITHIN A RANGE
# 153=1*1*1+5*5*5+3*3*3
# 407=4*4*4+0*0*0+7*7*7

lower=int(input("Enter the Lower Limit : "))
upper=int(input("Enter the Upper Limit : "))

print("\nThe Armstrong Numbers within this range is/are :")

for num in range (lower,upper+1):
 order=len(str(num))
 temp=num
 sum=0
 
 while temp>0:
  digit = temp%10
  sum=sum+digit**order
  temp=temp//10
 
 if(num==sum):
  print(num)
 