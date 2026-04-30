#WAP TO ADD EACH LETTER OF A WORD INTO A LIST

List = []
 
# Traditional approach of iterating
for character in 'PYTHON':
 List.append(character)
print(List)

#List-Comprehension Method
List = [character for character in 'PYTHON']
print(List)