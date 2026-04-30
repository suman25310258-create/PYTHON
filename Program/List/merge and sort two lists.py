#WAP TO MERGE TWO LISTS AND THEN SORT IT

#Taking the inputs for the 1st List from the user
n1=int(input("How many elements you want to insert into 1st List : "))
list1=[]
for i in range(n1):
 ele1=int(input("Enter the integer elements: "))
 list1.append(ele1)
print("The 1st List is : ",list1)


#Taking the inputs for the 2nd List from the user
n2=int(input("How many elements you want to insert into 2nd List : "))
list2=[]
for j in range(n2):
 ele2=int(input("Enter the integer elements: "))
 list2.append(ele2)
print("The 2nd List is : ",list2)

#Method-1:- Merge two lists using '+' operator
mg=list1+list2
print("The Merged List is :",mg)

#Method-2:- Merge two lists using 'extend()' method
list1.extend(list2)
print("The Merged List is :",list1)

#Sort the merged list
mg.sort()
print("The sorted List is :",mg)


