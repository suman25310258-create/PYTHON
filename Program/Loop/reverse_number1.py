#WAP TO REVERSE AN INTEGER NUMBER (BOTH NEGATIVE AND POSITIVE)

num=int(input("Enter Integer Number : "))

#checking the number is negative or positive.
if num<0:
 sign=-1
else:
 sign=1
 
rev=0 #initialise the reverse variable
num=abs(num) #working with the positive number

while num!=0:
 digit=num%10
 rev=rev*10+digit
 num=num//10

rev=rev*sign  #restoring the sign

print("The Reverse Number is : ",rev)