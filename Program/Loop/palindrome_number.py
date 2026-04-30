#WAP TO CHECK PALINDROME NUMBER

num=int(input("Enter Integer (+)ve Number : "))
temp=num
sum=0

while num>0:
 rev=num%10
 sum=sum*10+rev
 num=num//10
 
if temp==sum:
 print("Palindrome Number")
else: 
 print("Not Palindrome Number")