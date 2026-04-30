#MAXIMUM-MINIMUM USING FOR LOOP

lst=[5,7,2,8,9,1,0,4,3,-5]

max_val=lst[0]
min_val=lst[0]

for i in lst:
 if i>max_val:
  max_val=i                      
 if i<min_val:     # else: min_val=i 
  min_val=i
    
print("Maximum value of the list :",max_val)
print("Minimum value of the list :",min_val)


     
    