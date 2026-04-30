#WAP TO CHECK IF STRING IS A PANGRAM(contains every letter of the alphabet).

s = "The quick brown fox jumps over the lazy dog"
s = s.lower()
for ch in ("abcdefghijklmnopqrstuvwxyz"):
 if ch not in s:
  print("Not a pangram.")
  break
else:
  print("It's a pangram!")