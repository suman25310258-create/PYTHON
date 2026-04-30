#WAP TO CHECK PALINDROME USING 'for()' LOOP

word=input("Enter a String : ")
reversed_word=""

for ch in word:
 reversed_word=ch+reversed_word
print(reversed_word)

if word==reversed_word: 
 print("The String is a Palindrome")
else:
 print("The String is not a Palindrome")  
    