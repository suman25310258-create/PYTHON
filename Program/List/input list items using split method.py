##WAP TO INPUT INTEGER ITEMS A LIST, USING 'split()' METHOD

#METHOD 1:- USING 'split()' METHOD.
n=int(input("How many numbers to enter : "))

#if entered numbers are more or less than 'n'
while True:
 numbers = input("Enter numbers (use 'space' to enter next number): ").split()
 if len(numbers) == n:
   break
 print(f"You entered {len(numbers)} numbers instead of {n}. Please try again.\n")

for i in range(n):    
 numbers[i]=int(numbers[i]) #without 'int',the output will be e.g:- ['2', '5', '8', '9'] 
print(numbers)

#METHOD 2:- USING 'spit()','map()','list()' METHOD.
num= list(map(int,input("Enters items (use 'comma' to enter next number) :- ").split(",")))
print(num)