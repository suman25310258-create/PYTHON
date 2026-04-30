#WAP TO CONVERT INTO LIST FROM DICTIONARY

dic={1:"Mohit",2:"Rohit",3:"Virat"}

#Method 1:- Using list() & item() method
lst1=list(dic.items())
print(lst1)

#Method 2:- Using list comprehension
lst2=[(key,value) for key,value in dic.items()]
print(lst2)

#Method 3:- Using zip() function
lst3=zip(dic.keys(),dic.values())
lst3=list(lst3)
print(lst3)

#Method 4:- Using map() function
lst4=list(map(list,dic.items()))
print(lst4)

#Method 5:- Using 'for' loop & items() method
lst5=[]
for key,val in dic.items():
 lst5.append([key,val])
print(lst5) 
