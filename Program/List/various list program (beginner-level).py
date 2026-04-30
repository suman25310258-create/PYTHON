#WAP TO SHOW VARIOUS ACTIVITIES ON 'LIST'
#-------------------------------------------------------#
#Find the length of the list without 'len()' function
a = [10, 20, 30, 40, 50]
count = 0
for i in a:    
 count += 1
print("Length of list:", count)
#------------------------------------------------------#
#Find the reverse list of 'a' without using 'reverse()'
a = [10, 20, 30, 40, 50]
reversed_list = a[::-1]
print(reversed_list)
#------------------------------------------------------#
#Find if the number '40' exists in 'a' or not !!
a = [10, 20, 30, 40, 50]
if 40 in a:
 print("Found!")
#------------------------------------------------------#
# Find maximum and minimum without 'max()', 'min()' 
nums = [10, 3, 56, 1, 78, 23]
max_num = nums[0]
min_num = nums[0]
for n in nums:
 if n > max_num:
   max_num = n
 if n < min_num:
   min_num = n
print("Max:", max_num, "Min:", min_num)
#-------------------------------------------------------#
#Given numbers = [1, 2, 3, 4, 5], append 6 and 7 to it.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.append(7)
print(numbers)
#-------------------------------------------------------#
#Write a program to Replace third element with '20'
numbers = [1, 2, 3, 4, 5]
numbers[2] = 20
print(numbers)
#-------------------------------------------------------#
