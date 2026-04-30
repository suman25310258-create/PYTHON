#WAP TO FIND SUM OF ALL ODD-NUMBERS BETWEEN 1-50
#-----------------------------------------------#

#USING for() LOOP
#---------------#
total = 0
for i in range(1,51):
    if i%2!=0:
        total=total+i
print(total)


#USING while() LOOP
#-----------------#
a=1
total=0
while a<=50:
    if a%2!=0:
        total=total+a
    a=a+1    
print(total)        