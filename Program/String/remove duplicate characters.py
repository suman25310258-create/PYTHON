#WAP TO REMOVE DUPLICATE CHARACTERS FROM A STRING

s = "programming"
result = ""
for ch in s:
 if ch not in result:
  result += ch
print("After removing duplicates:", result)
