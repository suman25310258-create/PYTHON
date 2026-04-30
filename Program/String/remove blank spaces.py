#WAP TO REMOVE ALL SPACES FROM THE GIVEN STRING

#Method-1:-Using for() loop
s = "P y t h o n  Program"
new_s = ""
for ch in s:
 if ch != " ":
   new_s += ch
print("After removing spaces:", new_s)


#Method-1:-Using 'replace()' function
s = "P y t h o n  Program"
new_s = s.replace(" ", "")
print("After removing spaces:", new_s)

