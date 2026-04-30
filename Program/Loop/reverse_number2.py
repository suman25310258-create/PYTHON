#WAP TO REVERSE AN INTEGER NUMBER (BOTH NEGATIVE AND POSITIVE)

num=int(input("Enter Number : "))
rev=" "

#convert the absolute value of the number to a string.
#and loop through each digit.
for digit in str(abs(num)):
 rev=digit+rev
 
rev=int(rev) #convert reversed string back to integer 

#checking for negative number
if num<0:
 rev=-rev

print("The Reverse Number is :",rev)


