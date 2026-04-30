#WAP TO PRINT STAR LIKE:-
'''         5 4 3 2 1 
            4 3 2 1   
            3 2 1     
            2 1       
            1        ''' 

for i in range(1,6):
 k=6-i   
 for j in range(1,6):
  if j<=6-i:
    print(k,end=' ')
    k=k-1
  else: 
    print(" ",end=' ')
 print() 
