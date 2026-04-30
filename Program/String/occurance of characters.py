#WAP TO COUNT HOW MANY TIMES EACH CHARACTER APPEARS 
#--------------------------------------------------#

#METHOD-1 :- Using a for loop with dictionary
s = "banana"
freq = {}
for ch in s:
 if ch in freq:
  freq[ch] += 1
 else:
  freq[ch] = 1
print(freq)
print("\n")

#METHOD-2 :-Using count() inside a loop
s = "banana"
for ch in set(s):   # use set() to avoid duplicates
 print(ch, ":", s.count(ch))
 
print("\n") 

#ALSO FIND CHARACTERS THAT APPEAR MORE THAN ONCE
#----------------------------------------------#
for ch in set(s): 
 if s.count(ch) > 1:
  print(ch, "→ appears more than once")