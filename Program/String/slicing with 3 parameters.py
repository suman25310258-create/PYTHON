#WAP TO DEMONSTRATE SLICING WITH 3-PARAMETERS 

x= "I LOVE PYTHON"

#slicing with (+)ve indexes with 3 parameters 
print(x[0:8:2]) #start index=0,stop index=8-1,step jump=2.
print(x[0:6:1]) #start index=0,stop index=6-1,step jump=1(default)
print(x[2::8])  #start index=2,stop index=upto the end, step jump=8
print(x[2::])   #start index=1,stop index=upto end, step jump=1(default)
print(x[:8:])   #start index=0,stop index=8-1, step jump=1(default value)
print(x[::3])   #start index=0,stop index=upto end, step jump=3
print(x[::])    #start index=0,stop index=upto end, step jump=1(default)

print()

#slicing with (-)ve 3rd parameters 
print(x[8:1:-2]) #(-)ve 3rd index implies the direction right->left
print(x[5:0:-1])
print(x[::-1])   #Reversing whole string

print()

#slicing with (-)ve 2nd parameters 
print(x[8:-1:2])  #start index=8,stop index=(-1-1)=-2, step jump=1(default=1)
print(x[7:-2:])   #start index=7,stop index=(-2-1)=-3, step jump=1(default=1)
print(x[:-2:])

print()

#slicing with (-)ve 1st parameters 
print(x[-2:-5:-3])
print(x[-2:5:-3])
