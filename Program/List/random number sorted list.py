#GENERATE RANDOM NUMBERS FROM (1-20) AND APPEND THEM IN A LIST, AND SORT THE LIST

import random
n=int(input("Enter the total number of elements you want to insert : "))
l=[]
for i in range(0,n):
 rn=random.randint(1,n)
 l.append(rn)
print("The Random Number List is : ",l)

l.sort()
print("The Sorted List is : ",l)
