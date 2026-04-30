#WAP TO SORT THE CHARACTERS OF A STRING IN ALPHABETICAL ORDER.


#Method-1:-Using 'BUBBLE' sorting
#------------------------------#
string = "python"
# Convert string to list (since strings are immutable)
chars = list(string)

# Bubble sort
for i in range(len(chars)):
 for j in range(i + 1, len(chars)):
   if chars[i] > chars[j]:
     chars[i], chars[j] = chars[j], chars[i]

# Join back into a string
sorted_string = ''.join(chars)
print("Sorted string:", sorted_string)

print("\n")


#Method-2:-Using 'sorted()' and 'join()' functions
#---------------------------------------------#
string = "python"
sorted_string = ''.join(sorted(string))
print("Sorted string:", sorted_string)


print("\n")


#Method-3:-Using 'for' loop and 'sorted()' functions
#----------------------------------------------#
string = "python"
result = ""
for ch in sorted(string):
    result += ch
print("Sorted string:",(result))

print("\n")


#Method-4:-Using ''.join(sorted(string.lower())) (ignore case)
#------------------------------------------------------------#
string = "PyThOn"
sorted_string = ''.join(sorted(string.lower()))
print("Sorted string:",sorted_string)


print("\n")


#Method-5:-Using 'list()' and 'sort()'
#-----------------------------------#
string = "python"
char_list = list(string)
char_list.sort()
sorted_string = ''.join(char_list)
print("Sorted string:",(sorted_string))
