#WAP TO DEMONSTRATE FOR-LOOP WITH SLICING
#---------------------------------------#

#FOR LOOP OVER A SLICED LIST
#---------------------------#
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in nums[2:8]:
 print(i,end =" ")
print("\n")

#FOR LOOP WITH START:STOP:STEP
#----------------------------#
for i in nums[1:10:2]:
 print(i,end =" ")
print("\n")

#LOOP THROUGH ALTERNATIVE ELEMENTS
#--------------------------------#
for i in nums[::2]:
 print(i,end=" ")
print("\n")

#REVERSE LOOP USING SLICING
#-------------------------#
for i in nums[::-1]:
 print(i,end=" ")
print("\n") 

#FOR LOOP WITH SLICING ON A STRING
#--------------------------------#
name = "PYTHON"
for ch in name[1:5]:
 print(ch,end=" ")
print("\n")

#USING SLICING WITH 'range()' INDIDE A LOOP
#-----------------------------------------#
for i in list(range(1, 21))[::3]:
 print(i,end=" ")
 
 
