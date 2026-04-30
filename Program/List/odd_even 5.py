#WAP TO SEPARATE A LIST OF NUMNERS (1 TO 15) INTO TWO LISTS,ODD AND EVEN

li= list(range(1,15+1))

print("Original List is: ",li)

even_list=[]
odd_list=[]

for num in li:
 if num%2==0:
  even_list.append(num)
 else:
  odd_list.append(num)   

print("Even Number List is: ",even_list)
print("Odd Number List is: ",odd_list)   
