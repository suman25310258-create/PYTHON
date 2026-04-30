#WAP TO SHOW THE RESULTS OF THE FOLLOWING LOOP

lst=[3,4,6,8,9]

for i in lst:
  lst[-1]=i
print(lst)

for i in range(len(lst)):
  lst[-1]=i
print(lst)  