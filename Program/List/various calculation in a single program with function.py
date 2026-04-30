#WAP TO SHOW VERIOUS CALCULATION ON LIST(user input)
#--------------------------------------------------#

import math

# Function to calculate squares
def get_squares(lst):
    return [i*i for i in lst]

# Function to calculate factorials
def get_factorials(lst):
    return [math.factorial(num) for num in lst]

# Function to calculate sum
def get_sum(lst):
    return sum(lst)

# Function to segregate odd and even numbers
def segregate(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    return even, odd

# Function to convert to tuple
def to_tuple(lst):
    return tuple(lst)

# Function to convert to set
def to_set(lst):
    return set(lst)


# ----------------------- MAIN PROGRAM -------------------------------
def main():
    x = list(map(int, input("Enter Numbers (use space) : ").split()))
    print("The List is :", x)

    print("Square of each item of the List is :", get_squares(x))
    print("Factorial of each item of the List is :", get_factorials(x))
    print("The Sum of all items of the List is :", get_sum(x))

    even, odd = segregate(x)
    print("Even-Numbers List is :", even)
    print("Odd-Numbers List is :", odd)

    tup = to_tuple(x)
    print("The Tuple after conversion is :", tup)
    print("The Type after conversion is :", type(tup))

    s = to_set(x)
    print("The Set after conversion is :", s)
    print("The Type after conversion is :", type(s))


# Call main() function
main()

