#WAP FOR A SIMPLE CALCULATOR

print("1.Addition\n"
      "2.Subtract\n"
      "3.Multiplication\n"
      "4.Division")

c=input("\nEnter the operation you want to perform(1/2/3/4): ")

if(c=='1'):
 a=eval(input("\nEnter 1st number:"))
 b=eval(input("Enter 1st number:"))
 print("\nThe Addition of these 2 numbers is:",a+b)
elif(c=='2'):
 a=eval(input("\nEnter 1st number:"))
 b=eval(input("Enter 1st number:"))
 print("\nThe Subtraction of these 2 numbers is:",a-b)
elif(c=='3'):
 a=eval(input("\nEnter 1st number:"))
 b=eval(input("Enter 1st number:"))
 print("\nThe Multiplication of these 2 numbers is:",a*b)
elif(c=='4'):
 a=eval(input("\nEnter 1st number:"))
 b=eval(input("Enter 1st number:"))
 print("\nThe Division of these 2 numbers is=",a/b)
else:
  print("\nInvalid Choice")  