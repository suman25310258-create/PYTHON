#WAP TO DEMONSTRATE SLICING WITH 2-PARAMETERS 

x= "I LOVE PYTHON"

#slicing with (+)ve indexes with 2 parameters 
print(x[0:5])
print(x[2:6])
print(x[:6])  #stop value = 6-1= 5th no.index
print(x[0:])  #items start through the rest of the array
print(x[1:])  #items start through the rest of the array
print(x[:])   #copy of the whole array

print()

#slicing with (-)ve indexes with 2 parameters 
print(x[2:-2])
print(x[0:-1])  #same as print(x[:-1])
print(x[5:-1])
print(x[-5:-1])