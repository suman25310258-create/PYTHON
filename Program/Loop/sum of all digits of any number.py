#SUM OF THE ALL DIGITS OF ANY NUMBER

num=int(input("Enter any Number : "))

original_num=num

sum=0

while num>0:
 digit = num%10
 sum=sum+digit
 num=num//10

print(f"\nSum of all digits of {original_num} is : {sum}")