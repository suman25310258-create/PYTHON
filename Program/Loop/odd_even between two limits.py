#WAP TO SEGREGATE ODD-EVEN NUMBERS BETWEEN A RANGE OF NUMBERS

lower=int(input("Enter the lower Limit : "))
upper=int(input("Enter the upper Limit : "))

print("EVEN NUMBERS ARE")
for i in range(lower,upper+1):
 if i%2==0:
   print(i,end=" ")
   
print("\n")

print("ODD NUMBERS ARE")      
for i in range(lower,upper+1):
 if i%2!=0:
   print(i,end=" ")      