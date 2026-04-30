#WAP TO DETERMINE WHETHER A NUMBER IS A PRIME OR NOT

num=int(input("Enter an integer greater than 1 = "))

flag=False 
if(num>1):
 for i in range(2,num-1):
  if(num%i==0):
   flag=True 
   break 

if flag:
 print("It is not a Prime Number")
else:
 print("It is a prime Number")   
   