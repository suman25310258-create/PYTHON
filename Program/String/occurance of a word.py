#WAP TO COUNT HOW MANY TIMES A SPECIFIC WORD APPEARS IN A STRING.
#----------------------------------------------------------------#

s = "python is easy to learn. i love to study python"
word = "python"
count = 0

words = s.split()
print(words)

for w in words:
 if w == word:
  count += 1

print("\n")

print(f"'{word}' occurs {count} times")


