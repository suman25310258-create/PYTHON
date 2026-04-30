#WAP TO CALCULATE SUM OF DIGITS OF 3digit NUMBER

num=int(input("Enter any 3digit Number : "))
sum=0

#Method:-1
a=int(num/100)
b= int((num%100)/10)
c=(num%10)%10
sum=a+b+c
print("The Sum of the digits of",num,"is :",a,"+",b,"+",c,"=",sum)

#Method:-2
a=num//100
b=(num//10)%10
c=(num%100)%10
sum=a+b+c
print(f"The Sum of the digits of {num} is : {a} + {b} + {c} = {sum}")


