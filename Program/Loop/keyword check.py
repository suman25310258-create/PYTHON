#WAP TO CHECK A VALID KEYWORD FROM A LIST OF STRINGS

import keyword
words=["continue","python","break","java","css","global","lambda"]

#To find all the keywords in python
#print(keyword.kwlist)

for i in range(len(words)):
 if keyword.iskeyword(words[i]):
   print(words[i],"is a python keyword")
 else:
   print(words[i],"is not a python keyword")
