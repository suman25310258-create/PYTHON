# FACTORS OF A NUMBER

num= int(input("Enter any Integer : "))
print("The Factors of this Number are :")
for i in range(1,num+1):
 if(num%i==0):
  print(i)