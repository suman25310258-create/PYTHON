#WAP TO COUNT NUMBER OF VOWELS

n=input("Enter the String input : ")
vowel=['a','e','i','o','u','A','E','I','O','U']

count=0
for i in n:
 if i in vowel:  
  count=count+1
  print(i,end=' ')  
print("\nTotal Number of vowels in ",n,"is :", count)
print(f"Total Number of vowels in {n} is: {count}")
