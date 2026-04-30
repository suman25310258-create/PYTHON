#WAP TO SEGREGATE EVEN AND ODD LIST(INPUTS TAKEN FROM USER)

#input list elements from user
n=int(input("How many elements you want to enter : "))
lst=[]
for i in range(n):
 ele=int(input("Enter the Elements :"))
 lst.append(ele)
print("My List is : ",lst)

#segregate into two list(even and odd)
evenlst=[]
oddlst=[]
for i in lst:
 if i%2==0:
  evenlst.append(i)
 else:
  oddlst.append(i)
  
print("The Even List is : ",evenlst)
print("The Odd List is :", oddlst)
