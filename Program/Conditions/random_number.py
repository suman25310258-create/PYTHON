# WAP TO GENERATE RANDOM NUMBER GUESSING

import random
cnumber=random.randint(1,20) # You can also use randrange() method
userinput=int(input("Enter any Number between 1-20 : "))

print("Computer number is :",cnumber) 

if (cnumber>userinput):
 print("Your guess number is lesser than compuer number.")
elif (cnumber<userinput):    
 print("Your guess number is higher than computer number.")
else:
 print("Your guess number is correct")
 