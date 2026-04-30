# WAP TO FIND SUMMATION OF SERIES OF NUMBERS USING RECURSION
#-----------------------------------------------------------#

def f(n):
 if n == 0:  # Base condition (stop condition)
   return 0
 return n + f(n-1) # Recursion

num=int(input("ENTER THE Limit : "))  
sum=f(num)

print("THE SERIES AND It's SUM IS: ",end ="")
for i in range(1,num+1):
  if i == num:
    print(i, end=" ")
  else:     
    print(i,"+ ",end=" ")
      
print("=",sum)