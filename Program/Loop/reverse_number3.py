#WAP TO REVERSE ANY NUMBER IN PYTHON

num = int(input("Enter Integer (+)ve Number: "))
original = num  # Keep a copy of the original number
rev = 0

while num > 0:
 digit = num % 10
 rev = rev * 10 + digit
 print(digit, end="")  # Print digits in reverse order
 num = num // 10

# Now check with original number
if original == rev:
    print("\nPalindrome")
else:
    print("\nNot Palindrome")

