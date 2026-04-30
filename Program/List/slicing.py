#WAP TO DEMONSTRATE LIST SLICING

x= ["java","css","python","php","html","javascript","ruby"]

#slicing with (+)ve indexes with 2 parameters 

print(x[2:6])   
print(x[:6])    
print(x[0:])    
print(x[:])     

print()

#slicing with (-)ve indexes with 2 parameters 
print(x[2:-2])
print(x[0:-1])  #same as print(x[:-1])
print(x[-4:0])
print(x[-5:-1])
print(x[:-4])
print(x[-4:])

print()

#slicing with 3 parameters
print(x[2:6:2])
print(x[5:1:-1])
print(x[-4:0:-1])
print(x[-4:0:-4])
print(x[-6:-2:])
print(x[::])
print(x[:-2:])
print(x[::-1])
print(x[-5::]) 