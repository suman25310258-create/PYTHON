#WAP TO PRINT STAR LIKE:-
'''           *
              *  *
              *  *  *
              *  *  *  *
              *  *  *  *  *
                             '''

rows= int(input("Enter number of rows: "))

for i in range(1,rows+1):
 for j in range(1,i+1):
   if(j<=i):    
    print("*", end=" ")
 print() 