#WAP TO ACCESS LIST ELEMENTS USING INDEXING

#accessing the list elements with index number
list1=["java","python", "php","html","css"]
print(list1[1])
print(list1[4])

#accessing the elements from multi-dimensional list 
list2 =[[0,1,2],3,4,[5],[6,7]]
print(list2[0][2])
print(list2[4][1])

#accessing the elements from nested multi-dimensional list 
list3=[[0,1,2],3,4,[5],[[6,7,8,9]]]
print(list3[0][2])
print(list3[1])
print(list3[3][0])
print(list3[4][0][2])

#accessing the elements using (-)ve indexing
list4 = [1, 2, 'PYTHON', 4, 'JAVA', 6, True]
print(list4[-1])   # can also be written as print(list4[len(list4)-1])
print(list4[-3])   #can also be written as print(list4[len(list4)-3])
print(list4[-5])   #can also be written as print(list4[len(list4)-5])
