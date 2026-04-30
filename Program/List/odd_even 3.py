#SEPARATING EVEN & ODD NUMBER LIST UPTO 20

lst=list(range(1,21))
even=[]
odd=[]

for i in lst:
 if i%2==0:
  even.append(i)
 else:
  odd.append(i)
  
print("The Original List is:",lst)
print("\nThe Even Number List is:",even)
print("\nThe Odd Number List is:",odd)
  
     