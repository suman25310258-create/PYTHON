#WAP TO SWAP THE CASE OF ALL CHARACTERS
#--------------------------------------#

s = "PyThOn ProGRam"
swapped = ""

for ch in s:
 if ch.islower():
   swapped += ch.upper()
 elif ch.isupper():
   swapped += ch.lower()
 else:
   swapped += ch

print("Swapped case:", swapped)
