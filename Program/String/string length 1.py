#WAP TO FIND THE LENGTH OF A STRING

#Method1:- Using for loop
str=input("Enter any String : ")
print("String you enter is :",str)
count=0
for i in str:
 count=count+1
print("The Length of the String is :",count) 

#Method2:- Using len() function
length=len(str)
print("The Length of the String is :",length)