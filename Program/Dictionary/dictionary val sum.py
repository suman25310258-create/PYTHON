#WAP TO FIND THE SUM OF VALUES OF A DICTIONARY

n=int(input("How many key-value pair in your Dictionary : "))
d={}
for i in range(n):
 p=input("Enter the key : ")
 q=int(input("Enter the values(integer) : "))
 d.update({p:q})
print("My Dictionary is : ",d)

print()

#METHOD-1: FINDING THE SUM USING 'sum()' FUNCTION  
val_sum=sum(d.values()) # For find the sum of keys-> sum(d.keys())
print("The Sum of values of the above Dictionary is : ",val_sum)


#METHOD-2: FINDING THE SUM USING 'for()' LOOP      
total = 0
for val in d.values():
    total = total + val
print("The Sum of values of the above Dictionary is :", total)    