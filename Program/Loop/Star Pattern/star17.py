#WAP TO PRINT STAR LIKE:-
'''        1       
         1 2 3     
       1 2 3 4 5   
     1 2 3 4 5 6 7   '''

             
for i in range(1,5):
 k=1   
 for j in range(1,8):
  if j>=5-i and j<=3+i:
    print(k,end=' ')
    k=k+1
  else: 
    print(" ",end=' ')
 print() 