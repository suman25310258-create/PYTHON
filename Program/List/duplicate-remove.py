# REMOVE THE DUPLICATE ITEM OF THE LIST AND ALSO SORT THE NEW LIST

#Method 1:- Using for-loop
MyLst=[2,2,3,4,5,3,7,8,7,1,1,9,4,3,2,7,8]

NewLst=[]
for i in MyLst:
 if i not in NewLst:
    NewLst.append(i)
print("The List not having duplicate items is : ",NewLst)

#Method 2:- Using set() function
lst = list(set(MyLst))

#This approach does not preserve the original order.
print("The List not having duplicate items is : ",lst)

#Method 3:- Using List-Comprehension
lstcom=[]
[lstcom.append(i) for i in MyLst if i not in lstcom]
print("The List not having duplicate items is : ",sorted(lstcom))


#Method 4:- Using Dictionary fromkeys()
L=list(dict.fromkeys(MyLst))
print("The List not having duplicate items is : ",L)
