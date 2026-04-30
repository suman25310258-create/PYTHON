from add import*
from sub import*
from mul import*
from div import*

while True:    
 print("What do you want to do ?")
 print("1.Addition")
 print("2.Subtract")
 print("3.Multiplication")
 print("4.Division")
 print("Enter Q to Exit.")

 choice=input("Enter Your Choice : ")
 if (choice=="Q" or choice=="q"):
   print("EXIT CALCULATOR")   
   break
 if choice in ['1', '2', '3', '4']:
   num1=int(input("Enter the 1st number: "))
   num2=int(input("Enter the 2nd number: "))

 if(choice=='1'):
  add(num1,num2)
 elif(choice=='2'):
  sub(num1,num2)
 elif(choice=='3'):
  mul(num1,num2)
 elif(choice=='4'):
  div(num1,num2)
 else:
  print("Wrong Choice! Please enter 1–4 or Q to quit.")

 print("\n")
  