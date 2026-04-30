# WAP TO FIND THE LENGTH AND THE LAST ELEMENT OF THE FOLLOWING LIST

ls=[2,3,4,5,6,7,8]

#Using 'len()' function and positive indexing
length=len(ls)
last=ls[length-1] #same as last=ls[-1]
print("Total Number of Elements in the list :",length)
print("Last Element of the list is :",last)

#Using Loop and positive indexing
length = 0
for x in ls:
 length=length+1
last=ls[length-1] 
print("\nThe Number of Elements in the list :",length)
print("Last Element of the list is :",last)


#Using 'len()' function and Negative Indexing 
length=len(ls)
last=ls[-1]
print("\nThe Number of Elements in the list :",length)
print("Last Element of the list is :",last)