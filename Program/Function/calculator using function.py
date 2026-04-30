#WAP A CALCULATOR USING FUNCTION

def addition(x,y):  
 print("Addition of two Numbers is:",x+y)
 
def subtraction(x,y):
 print("Subtraction of two Numbers is:",x-y)

def multiplication(x,y):
 print("Multiplication of two Numbers:",x*y)

def division(x,y):
 print("Division of two Numbers:",round(x/y,2)) #rounded upto 2 decimal point
 
def MENU():
 print('''
        1.Addition
        2.Subtract
        3.Multiplication
        4.Division''')
 
 choice=input("\nEnter the operation you want to perform(1/2/3/4):-")
 
 if(choice=='1'):
  x=eval(input("Enter 1st Integer:"))
  y=eval(input("Enter 2nd Integer:"))   
  addition(x,y)
 elif(choice=='2'):
  x=eval(input("Enter 1st Integer:"))
  y=eval(input("Enter 2nd Integer:"))    
  subtraction(x,y)
 elif(choice=='3'):
  x=eval(input("Enter 1st Integer:"))
  y=eval(input("Enter 2nd Integer:"))   
  multiplication(x,y)
 elif(choice=='4'):
  x=eval(input("Enter 1st Integer:"))
  y=eval(input("Enter 2nd Integer:")) 
  division(x,y)
 else:
  print("Invalid Choice")   
   
MENU()