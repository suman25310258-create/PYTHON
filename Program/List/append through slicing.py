#APPEND ITEMS WITH THE HELP OF 'append()' METHOD
#'append()' METHOD ALWAYS ADD ITEMS AT THE END OF THE LIST
lst=[11,22,33,44,55]
lst.append(66)         #adding 66 at the end of the 'lst'
lst.append((77,88))    #adding tuple at the end of the 'lst'
lst.append([99,111])   #adding another list at the end of the 'lst'
lst.append({120,125})  #adding a set at the end of the 'lst'
print(lst)

#APPEND ITEM WITH THE HELP OF SLICING
#SLICING IS MORE EFFICIENT THAN 'append()' METHOD, AS IT CAN APPEND AT ANY POSITION
lst1=[2,3,4,5,6]

#insert at the end of the list
lst1[len(lst1):]=[7] #equivalent to lst1.append(7)
print(lst1)

#insert 10 between 4 and 5
lst1[3:3]=[10]
print(lst1)

#insert 1 at the beginning of the list
lst1[:0]=[1]
print(lst1)