#WAP TO FIND THE INTERSECTION (COMMON) OF TWO LISTS

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

#METHOD1:-WITH NESTED LOOP WITH "in" 
common = []
for x in a:
 for y in b:
   if x == y:   
     common.append(x)

print(common)

#METHOD2:-SINGLE LOOP WITH "in" 
common = []
for x in a:
    if x in b:
        common.append(x)

print(common)