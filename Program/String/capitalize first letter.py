#CAPITALIZE THE FIRST LETTER OF EACH WORD IN A STRING.

#Method-1:-Using 'title()' function
s = "python is fun to learn"
new_s = s.title()
print("After capitalizing:", new_s)


#Method-2:-Using 'split()' and 'capitalize()' function
s = "python is fun to learn"
words = s.split()
new_s = ""
for w in words:
 new_s += w.capitalize() + " "
print("After capitalizing:", new_s.strip())