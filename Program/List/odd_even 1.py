#WAP TO SEGREGATE EVEN AND ODD LIST

list=[1,2,3,4,5,6,7,8,9]
evenlst=[]
oddlst=[]

for i in list:
 if i%2==0:
  evenlst.append(i)
 else:
  oddlst.append(i)

print("The Even List is : ",evenlst)
print("The Odd List is :", oddlst)