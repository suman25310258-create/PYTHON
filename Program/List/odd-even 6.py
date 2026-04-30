#SEPARATE TWO ODD-EVEN NUMBER LIST FROM USER-DEFINED LIST

Mlist=list(map(int, input("Enter elements (comma-separated): ").split(',')))
print("The main list is :",Mlist)


even_list=[]
odd_list=[]

for num in Mlist:
 if num%2==0:
  even_list.append(num)
 else:
  odd_list.append(num)   

print("Even Number List is: ",even_list)
print("Odd Number List is: ",odd_list)   

