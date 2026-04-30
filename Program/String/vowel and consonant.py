#COUNT THE NUMBER OF VOWELS AND CONSONANTS IN A STRING.
#-----------------------------------------------------#

s = "Python"
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in s:
  if (char.isalpha() and (char in vowels)): 
    v_count += 1
  else:
    c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
