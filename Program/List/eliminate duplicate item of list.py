#WAP TO ELIMINATE DUPLICATE ITEM OF LIST

lst=[3,4,5,5,6,7,8,9,9,"python","java","java",True]

#convert the 'list' in 'set'
#set excludes the duplicate items
non_dupli_set=set(lst)
print(non_dupli_set)

print("\n")

#convert the set in list again 
non_dupli_list=list(non_dupli_set)
print(non_dupli_list)    