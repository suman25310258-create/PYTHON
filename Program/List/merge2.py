#WAP TO MERGE TWO LISTS USING BUILT-IN FUNCTIONS

#Method-1:- Merge two lists using 'append()' method
list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list2:
 list1.append(i)
print("The Merged List is :",list1)

#Method-2:- Merge two lists using 'extend()' method

list3 = [1, 2, 3]
list4 = [4, 5, 6]

list3.extend(list4)
print("The Merged List is :",list3)

