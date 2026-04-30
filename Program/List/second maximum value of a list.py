#WAP TO FIND 2ND MAXIMUM VALUE OF A LIST

my_list = [5, 8, 2, 1, 9, 10]

# initialize the maximum and second maximum values with the first two elements of the list
if my_list[0] > my_list[1]:
 max_value = my_list[0]
 second_max_value = my_list[1]
else:
 max_value = my_list[1]
 second_max_value = my_list[0]

# iterate through the rest of the list and update the maximum and second maximum values
for num in my_list[2:]:
 if num > max_value:
  second_max_value = max_value
  max_value = num
 elif num > second_max_value:
  second_max_value = num

print("Second highest value in the list:", second_max_value)





