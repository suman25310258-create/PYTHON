#WAP TO DISPLAY FIBONACCI SERIES UPTO A CERTAIN NUMBER
# 0 1 1 2 3 5 8 13......
# 0,1,(0+1),(1+1),(1+2),(2+3),(3+5),(5+8)........

a=0
b=1
num=int(input("Enter a number to obtain Fibonacci series : "))

if num==1:
 print(a)
else:
 print(a)
 print(b)

for i in range(2,num):
  c=a+b
  a=b
  b=c
  print(c)
  
 
        