#CONVERT "aaabbccaaa" → "a3b2c2a3" (count consecutive characters).

#METHOD-1:-Using 'for()' loop
s = "aaabbccaaa"
result = ""
count = 1
for i in range(len(s)):
 # Check if next character is same
 if i + 1 < len(s) and s[i] == s[i + 1]:
  count += 1
 else:
  result += s[i] + str(count)
  count = 1  # reset for next char
print(result)


#METHOD-2:-Using 'itertools' loop
from itertools import groupby
s = "aaabbccaaa"
result = ""
for char, group in groupby(s):
 count = len(list(group))
 result += char + str(count)
print(result)
