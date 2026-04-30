#WAP TO CHECK PALINDROME USING INDEXING
# 191,MOM,RADAR,MADAM...etc.

n=input("Enter the input : ")

if str(n)==str(n)[::-1]:
 print("This is a palindrome")
else:
 print("This is not a palindrome")

