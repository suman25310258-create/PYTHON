'''WAP TO PRINT STAR LIKE :-    *       
                              * * *     
                            * * * * *   
                          * * * * * * * 
                          * * * * * * * 
                            * * * * *   
                              * * *     
                                *          '''

#1st half rectangle (star6.py)
for i in range(1,5):
 for j in range(1,8):
  if j>=5-i and j<=3+i :  
   print("*",end=' ')
  else:
   print(" ",end=' ')   
 print()
 
#2nd rectangle in reverse form (star7.py) 
for x in range(1,5):
 for y in range(1,8):
  if y>=x and y<=8-x :  
   print("*",end=' ')
  else:
   print(" ",end=' ')   
 print()    