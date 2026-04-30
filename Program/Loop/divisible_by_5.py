# WAP TO TO FIND NUMBERS(1 TO 100) DIVISIBLE BY 5

print("The Numbers Divisible by 5 are : ")
for i in range (1,100+1):
 if i%5==0:
  print(i)
  
# USING lambda & filter FUNCTION

l=[10,12,15,18,20,22,25,30]
result= list(filter(lambda x: x % 5==0,l))
print("The Numbers Divisible by 5 are : ",result)
