#WAP TO PRINT STAR LIKE:-
'''           1         
              2  4      
              3  6  9     
              4  8  12 16  
              5  10 15 20 25     '''
                                 

row=int(input("Enter the number of rows: "))

for i in range(1,row+1):
 for j in range(1,i+1):
  if j<=i:
    sqr=i*j
    print(sqr,end=' ')
  else:
    print(" ",end=' ')
 print()   