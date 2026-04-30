#WAP TO FIND LONGEST AND SHORTEST WORD IN A GIVEN STRING
#-------------------------------------------------------#

s = "I love playing cricket"
words = s.split()

#Method-1: Using max,min built-in functions
longest = max(words,key=len)
shortest = min(words,key=len)
print("Longest word:", longest)
print("Shortest word:", shortest)

print("\n")

#Method-1: Using 'for()' Loop
longest = shortest = words[0]
for word in words:
 if len(word) > len(longest):
  longest = word
 if len(word) < len(shortest):
  shortest = word

print("Longest word:", longest)
print("Shortest word:", shortest)


