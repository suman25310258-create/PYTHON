#WAP REPLACE EVERY OCCURANCE OF SUBSTRING WITH ANOTHER SUBSTRING(without using replace().
#---------------------------------------------------------------------------------------#

s = "I like Python. Python is fun."
old = "Python"
new = "Java"
parts = s.split(old)
result = new.join(parts)
print(result)

#WAP REPLACE EVERY OCCURANCE OF SUBSTRING WITH ANOTHER SUBSTRING(with 'replace()' function).
#------------------------------------------------------------------------------------------#
s = "I like Python. Python is fun."
old = "Python"
new = "Java"
result = s.replace(old, new)
print(result)
