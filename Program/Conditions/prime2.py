#WAP TO FIND WHETHER A NUMBER IS A PRIME OR NOT

num=int(input("Enter an Integer : "))

if(num==1):
 print("It is not a Prime Number")
 
if(num>1):
 for i in range(2,num):
  if(num%i==0):
   print("It is a not a Prime Number")
   break
 else:
   print("It is a Prime Number")   