#FACTORIAL OF A NUMBER USING FOR LOOP

num=int(input("Enter the Number :- "))
fact=1

if num<0:
 print("Factorial of a (-)ve Number does not exist.")

if num==0: 
 print("Factorial of",num,"is", 1)

if num>0: 
 for i in range(1, num+1):
  fact= fact*i    
 print("The factorial of the number is = ",fact)    