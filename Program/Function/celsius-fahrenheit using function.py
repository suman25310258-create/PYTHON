# WAP TO CONVERT CELSIUS TO FAHRENHEIT AND VICE-VERSA

def Celsius():
 C=int(input("\nEnter the temperature in Celsius : "))   
 F=(C/5*9)+32
 print("The Fahrenheit Temperature is = {:.2f}".format(F)) #upto 2 decimal place
 
def Fahrenheit():
 F=int(input("\nEnter the temperature in Fahrenheit : "))
 C=((F-32)/9)*5
 print("The Celsius Temperature is =",round(C,2))   #upto 2 decimal place
 
def choice():
  print('''
        1.Celsius to Fahrenheit
        2.Fahrenheit to Celsius''')
 
  opt=input("\nEnter the operation you want to perform(1/2):- ")

  if(opt=='1'):
   Celsius()
  elif(opt=='2'):
   Fahrenheit()
  else:
   print("Invalid Choice")  

choice()