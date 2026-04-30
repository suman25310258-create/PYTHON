#WAP TO COUNT UPPER-CASE AND LOWER-CASE LETTERS

s = "PyThon ProGRam"
u_count = 0
l_count = 0

for ch in s:
 if ch.isupper():
   u_count += 1
 if ch.islower():
   l_count += 1

print("Uppercase:", u_count)
print("Lowercase:", l_count)
