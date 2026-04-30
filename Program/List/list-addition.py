#WAP TO LIST ADDITION

n1= int(input("How Many Numbers in 1st List : "))
M=[]

for i in range(n1):
 num1=int(input("Enter Numbers: "))
 M.append(num1)
print("1st List is :",M)

n2= int(input("\nHow Many Numbers in 2nd List : "))
N=[]

for j in range(n2):
 num2=int(input("Enter Numbers: "))
 N.append(num2)
print("2nd List is :",N)

L=M+N
print("\nAddition of two Lists is :",L)
