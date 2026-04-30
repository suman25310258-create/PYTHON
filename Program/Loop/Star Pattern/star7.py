'''WAP TO PRINT STAR LIKE :-                          
                          
                          * * * * * * * 
                            * * * * *   
                              * * *     
                                *      '''


for x in range(1,5):
 for y in range(1,8):
  if y>=x and y<=8-x :  
   print("*",end=' ')
  else:
   print(" ",end=' ')   
 print()    