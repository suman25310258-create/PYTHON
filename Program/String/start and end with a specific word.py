#WAP TO CHECK IF THE GIVEN STRING START WITH OR END WITH A SPECIFIC WORD.

text = input("Enter a string: ")
word = input("Enter the word to check: ")

if text.startswith(word):
    print("The string starts with the given word.")
elif text.endswith(word):
    print("The string ends with the given word.")
else:
    print("The string neither starts nor ends with the given word.")
