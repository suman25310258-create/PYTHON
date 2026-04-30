#WAP TO FIND SUM AND AVERAGE OF NUMBERS

limit=int(input("Enter the Limit = "))
sum=0
for i in range(1,limit+1):
 sum=sum+i
 avg= sum/i
print("The Sum of 1 to",i,"is = ",sum)
print("The Average is",avg)
 