#WAP TO PRINT STAR LIKE (Butterfly):-
'''
             *           * 
             * *       * * 
             * * *   * * * 
             * * * * * * * 
             * * * * * * * 
             * * *   * * * 
             * *       * * 
             *           *   '''


#Copy from star4
for i in range(1,5):
 for j in range(1,8):
  if (j<=i or j>=8-i):
   print("*",end=' ')
  else: 
   print(" ",end=' ')
 print()     

#Copy from star3
for i in range(1,5):
 for j in range(1,8):
  if (j<=5-i or j>=3+i):
   print("*",end=' ')
  else: 
   print(" ",end=' ')
 print()     