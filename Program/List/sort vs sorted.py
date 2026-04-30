#WAP TO DEMONSTRATE THE DIFFERENCE BETWEEN 'sort()' and 'sorted()' FUNCTIONS

#sort the list items in ascending order
x=[23,56,20,12]
x.sort()
print(x)

#sort the list items in descending order
x=[23,56,20,12]
x.sort(reverse=True)
print(x)

#return the new sorted list,but does not sort the original list.
y=[30,20,40,10]
y1=sorted(y)
print(y1)
print(y) #original list is not sorted.