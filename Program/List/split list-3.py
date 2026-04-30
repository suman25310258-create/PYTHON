#WAP TO SPLIT ALTERNATIVE ELEMENTS INTO TWO LISTS USING LOOP, LAST ELEMENT OF
#EACH LIST WILL BE THE SUM OF THE ALL ELEMENTS OF THAT LIST

# Taking input from user
input_str = input("Enter elements separated by space: ")

# Converting input string to list of integers
original_list = list(map(int, input_str.split()))

#print(original_list)
print("Original List is :",original_list)

# Two empty lists to store alternate elements
list1 = []
list2 = []

# Splitting elements alternately using a loop
for i in range(len(original_list)):
 if i % 2 == 0:
   list1.append(original_list[i])
 else:
   list2.append(original_list[i])

# Appending the sum as the last element
list1.append(sum(list1))
list2.append(sum(list2))

# Printing the results
print("Alternative List 1:", list1)
print("Alternative List 2:", list2)