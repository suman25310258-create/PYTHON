#WAP TO FIND EVEN AND ODD NUMBER BETWEEN 1-10 USING LIST COMPREHENSION

#Find Even numbers between 1-10 using List-Comprehension
list = [i for i in range(1,11) if i % 2 == 0]
print("List of Even Numbers:- ", list)

#Find Odd numbers between 1-10 using List-Comprehension
list = [i for i in range(1,11) if i % 2 != 0]
print("List of Odd Numbers:- ",list)