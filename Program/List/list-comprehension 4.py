#WAP TO DEMONSTRATE LIST-COMPREHENSION

#Square of each element of the 'list'
list=[1,2,3,4,5]
list = [i*i for i in range(1,6)]
print("The Square-Eliment List is : ",list)

#Convert each element of 'list1' in upper case
list1=['apple','orange','banana']
list1 = [i.upper() for i in list1]
print(list1)

#Multiplication table of '10'
numbers = [i*10 for i in range(1, 11)]
print("Multiplication Table of number '10' is :",numbers)