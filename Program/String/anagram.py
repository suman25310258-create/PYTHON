#WAP TO CHECK IF TWO STRINGS ARE ANAGRAMS
#(Anagram → same letters in different order, e.g., “listen” & “silent”)

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):  #sorted(s1) → ['e','i','l','n','s','t']
 print("Anagram")             #sorted(s2) → ['e','i','l','n','s','t']
else:
 print("Not anagram")
