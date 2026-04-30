# Method-1:- WAP TO SWAP TWO VARIABLES USING THIRD VARIABLE
x,y=map(int,input("Enter Two Numbers X and Y (seperated by space):").split())
print("Before the swapping X->",x,"and Y->",y)
temp=x
x=y
y=temp
print("After the swapping :- X->",x,"and Y->",y)

# Method-2:-WAP TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE
x,y=map(int,input("Enter Two Numbers X and Y (seperated by space):").split())
print("Before the swapping X->",x,"and Y->",y)
x,y=y,x
print("After the swapping :- X->",x,"and Y->",y)

# Method-3:- WAP TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE
x,y=map(int,input("Enter Two Numbers X and Y (seperated by space):").split())
print("Before the swapping X->",x,"and Y->",y)
x=x+y
y=x-y
x=x-y
print("After the swapping :- X->",x,"and Y->",y)

# Method-4:- WAP TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE
x,y=map(int,input("Enter Two Numbers X and Y (seperated by space):").split())
print("Before the swapping X->",x,"and Y->",y)
x=x*y
y=x/y
x=x/y
print("After the swapping :- X->",x,"and Y->",y)