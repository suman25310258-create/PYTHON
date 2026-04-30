#WAP TO TURN EVERY ITEM OF A LIST INTO ITS SQUARE

#Method1:- Using List-Comprehension
#[expression for item in iterable]
lst=[1,2,3,4,5,6,7,8,9]
[print(i*i, end=' ') for i in lst]
print("\n")


#Method2:- Using simple 'for' loop
for i in lst:
 print(i*i,end=' ')
 
print("\n")

#Convert the result into a list again
l=[]
for i in lst:
 l.append(i*i)
print(l) 

#Method3:- Using 'function' and 'return' statement
def square(x):
 return x*x
result=list(map(square,lst))
print(result)




