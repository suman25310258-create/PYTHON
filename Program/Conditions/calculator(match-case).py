#WAP TO BUILD A SIMPLE CALCULATOR

print("1.Addition\n"
      "2.Subtract\n"
      "3.Multiplication\n"
      "4.Division")

operation=int(input("\nEnter the operation you want to perform(1/2/3/4): "))

match(operation):
 case 1:   
  a=int(input("\nEnter 1st number:"))
  b=int(input("Enter 1st number:"))
  print("\nThe Addition of these 2 numbers is:",a+b)
  
 case 2:
  a=int(input("\nEnter 1st number:"))
  b=int(input("Enter 1st number:"))
  print("\nThe Subtraction of these 2 numbers is:",a-b)
 
 case 3:
  a=int(input("\nEnter 1st number:"))
  b=int(input("Enter 1st number:"))
  print("\nThe Multiplication of these 2 numbers is:",a*b)
  
 case 4:
  a=int(input("\nEnter 1st number:"))
  b=int(input("Enter 1st number:"))
  print("\nThe Division of these 2 numbers is=",a/b)

 case _:
  print("\nInvalid Choice")  