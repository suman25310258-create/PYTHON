#WAP TO DEMONSTRATE 'accumulate()' FUNCTION

import itertools
import operator
GFG = [1, 2, 3, 4, 5]

#if no function is passed, addition takes place by default.
#that means (GFG) and (GFG,operator.add) are same
result1 = itertools.accumulate(GFG) 
result2 = itertools.accumulate(GFG,operator.mul)
result3 = itertools.accumulate(GFG,operator.sub)

#printing each item from list for result1
for i in result1:
 print(i,end=' ')

print()
    
#printing each item from list for result2
for i in result2:
 print(i,end=' ')

print()

#printing each item from list for result3
for i in result3:
 print(i,end=' ')
    
