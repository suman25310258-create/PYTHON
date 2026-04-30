#WAP TO PRINT STAR LIKE:-
'''             *
                * *
                * * *
                * * * *
                * * * 
                * *
                *           '''
                
#first triangle
for x in range(1,4):
 for y in range(1,5):
  if y<=x:
   print("*",end=" ")
  else: 
   print(" ",end='')
 print()     

#second triangle
for i in range(1,5):
 for j in range(1,5):
  if j<=5-i:
   print("*",end=" ")
  else: 
   print(" ",end='') 
 print()  