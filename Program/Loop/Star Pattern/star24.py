'''WAP TO PRINT STAR LIKE :-     * 
                               * * 
                             * * * 
                           * * * *     '''

x=int(input("Enter Number: "))

for i in range(1,x):
 for j in range(x,1,-1):
  if (i>=j):   
   print("*",end=' ')
  else:
   print(" ",end=' ')   
 print()    
