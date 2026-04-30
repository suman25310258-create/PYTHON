#WAP TO READ n AND COMPUTE n+nn+nnn USING STRING CONCATINATION
# 2+22+222, 5+55+555 .....etc.

num= int(input("Enter the value of 'n' : "))
temp=str(num)
temp1=temp+temp
temp2=temp+temp+temp

cal= num+int(temp1)+int(temp2)
print("The sum of :",temp,"+",temp1,"+",temp2, "is ->",cal)