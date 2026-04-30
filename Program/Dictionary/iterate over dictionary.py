#WAP TO ITERATE OVER DICTIONARY

employee={"Suman":"Engineer","Deepa":"Programmer","Ratna":"Analyst"}

#Method 1:- with items() method. 
for key,value in employee.items():
 print(key,":",value)
print("\n")
   
#Method 2:- with keys
for key in employee:
 print(key,"-",employee[key])
print("\n")

#Method 3:- with keys and values separately
for i in employee.keys():
 print(i)
print("\n")
for j in employee.values():
 print(j) 