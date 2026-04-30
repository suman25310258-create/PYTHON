#WAP TO FIND MAXIMUM-ITEM USING 'accumulator()' FUNCTION

import itertools
  
GFG = [5, 3, 6, 2, 1, 9, 1 ]
  
# now here no need to import operator
# as we are not using any operator
result = itertools.accumulate(GFG, max)
  
# printing each item from list
for each in result:
 print(each,end=' ')