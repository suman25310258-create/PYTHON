#WAP TO SEGREGATE EVEN-ODD NUMBER LIST AMONG INPUTTED NUMBERS

start=int(input("Enter the Starting Number : "))
end=int(input("Enter the ending Number : "))

evn=[]
odd=[]

for i in range(start,end+1):
 if i%2==0:
   evn.append(i)
 else:
   odd.append(i)

print("The Odd Numbers are :",odd)
print("The Even Numbers are :",evn)