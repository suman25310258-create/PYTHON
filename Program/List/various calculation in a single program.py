#WAP TO SHOW VERIOUS CALCULATION ON LIST(user input)
#--------------------------------------------------#
x=list(map(int,input("Enter Numbers (use space) : ").split()))
print("The List is : ",x)
#------------------------------------------------------------#
#SQUARE OF EACH ITEM IN THE LIST
sqrt=[]
for i in x:
 sqrt.append(i*i)
print("Square of each item of the List is : ",sqrt)
#-------------------------------------------------------------#
#FACTORIAL OF EACH ITEM IN THE LIST
facto=[]
for num in x:
 fact=1
 for i in range(1,num+1):
   fact=fact*i
 facto.append(fact)
print("Factorial of each item of the List is :",facto)
#--------------------------------------------------------------#
#SUM OF THE ITEMS IN THE LIST
sum=0
for i in x:
 sum=sum+i
print("The Sum of all items of the List is :",sum)
#---------------------------------------------------------------#
#ODD AND EVEN ITEM SEGREGATION
even=[]
odd=[]
for i in x:
 if i%2==0:
  even.append(i)
 else:
  odd.append(i)
print("Even-Numbers List is :",even)
print("Odd-Numbers List is :",odd)
#---------------------------------------------------------------#
#CONVERT THE LIST INTO TUPLE
tup=tuple(x)
print("The Tuple after conversion is :",tup)
print("The Type after convesion is :",type(tup))
#---------------------------------------------------------------#
#CONVERT THE LIST INTO SET
s=set(x)
print("The Set after conversion is :",s)
print("The Type after convesion is :",type(s))
#---------------------------------------------------------------#
