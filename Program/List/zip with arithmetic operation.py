#WAP TO DO ARITHMETIC OPERATION USING ZIP FUNCTION 

test_list1 = [3, 5, 2, 6, 4]
test_list2 = [7, 3, 4, 1, 5]
 
# using zip() + list comprehension
div = [i / j for i, j in zip(test_list1, test_list2)]
minus= [i-j for i, j in zip(test_list1, test_list2)]
add=[i+j for i, j in zip(test_list1, test_list2)]
mul=[i*j for i, j in zip(test_list1, test_list2)]

# printing result
print ("The division list is : ",div)
print ("The division list is : ",minus)
print ("The division list is : ",add)
print ("The division list is : ",mul)