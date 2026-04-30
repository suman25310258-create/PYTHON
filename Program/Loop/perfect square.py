#WAP TO CHECK IF A NUMBER IS A PERFECT SQUAR
# 4=2x2  9=3x3 16=4x4 25=5x5

n=int(input("Enter any number  : "))
flag=0
for i in range(n):
 if i*i==n:
  flag =1
  break 

if flag==1:
 print(n,"is a perfect square number.")
 
else:
 print(n,"is not a perfect square number.")  