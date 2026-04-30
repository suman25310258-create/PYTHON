#WAP TO SEGREGATE EVEN NUMBER ONLY FROM GIVEN LIST

list=[1,2,3,4,5,6,7,8,9]

#Method1:- Using 'append()' method
evenlst=[]
for i in list:
 if i%2==0:
  evenlst.append(i)
print("The Even List is : ",evenlst)

#Method2:- Using 'list-comprehension'  method
list= [i for i in list if i % 2 == 0]
print("The Even List is : ",list)