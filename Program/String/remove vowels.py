#WAP TO REMOVE ALL VOWELS FROM A STRING

s = "Python programming is awesome"
vowels = "aeiouAEIOU"
result = ""

for ch in s:
 if ch not in vowels:
  result += ch

#After removing vowels --> 'a','e','i','o'
print("String without vowels:=>", result)
