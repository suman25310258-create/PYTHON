#WAP SHOWING 'range()' USED WITH SLICING
#--------------------------------------#
#Note:- 'range()' itself doesn’t support slicing directly, so we first convert it to a list#


#Example 1: Basic range with slicing
#----------------------------------#
numbers = list(range(1, 21))   # creates numbers from 1 to 20
print(numbers[::2])            # every 2nd element

#Example 2: Reverse using slicing
#--------------------------------#
numbers = list(range(1, 11))
print(numbers[::-1])

#Example 3: Odd numbers in reverse (range + slicing)
#--------------------------------------------------#
odd_numbers = list(range(1, 40, 2))
print(odd_numbers[::-1])

