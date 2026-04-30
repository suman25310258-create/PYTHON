#WAP TO INPUT INTEGER LIST ITEMS

#TAKING INPUT THROUGH 'for()' LOOP
n=int(input("How many numbers to enter : ")) 
num=[]
for i in range(n):
 x=int(input("Enter Numbers(next number after ENTER): "))
 num.append(x)
print("The List is :",num)

print("\n")

#TAKING INPUT THROUGH 'while()' LOOP
L=[]
C='Y'
while C=='Y' :
 x=int(input("Enter the Element : "))
 L.append(x)
 C=input("Enter 'Y' to continue :-").upper()
print("The List is :",L)

