#WAP TO REVERSE A STRING WITH SLICING AND WITH OUT SLICING (loop)

#Method-1: With Slicing
s=input("Enter any String : ")
reverse=s[::-1]
print("Reverse String is : ",reverse)

#Method-2: Without Slicing
rev = ""
for char in s:
  rev = char + rev
print("Reversed string is:", rev)
