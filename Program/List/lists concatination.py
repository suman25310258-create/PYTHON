#WAP TO CONCATINATE TWO LISTS

list1=['P','T','O']
list2=['Y','H','N']

#Method1:- Using List Compression and zip() function
[print(i+j, end='') for i,j in zip(list1,list2)]
print("\n")

#Method2:- Using simple 'for' loop and zip() function
for i,j in zip(list1,list2):
 print(i+j, end='')
print("\n")

#Method3:- Using simple 'for' loop  
for k in range(len(list1)):  #as length of list1=list2
 print(list1[k]+list2[k], end='')
 
 