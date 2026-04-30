#WAP TO REMOVE ALL PUNCTUATION FROM THE STRING
#--------------------------------------------#

import string

s = "Hello, World! Python."
new_s = ""
for ch in s:
 if ch not in string.punctuation:
   new_s += ch
print("After removing punctuation:", new_s)
