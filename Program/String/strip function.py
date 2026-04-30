#WAP TO REMOVE BLANK SPACES FROM BEGINNING AND END OF A STRING
#-------------------------------------------------------------#

s = "   Python Programming     "
new_s = s.strip()
print("After strip():", new_s)


#WAP TO REMOVE CHARACTERS FROM BEGINNING AND END OF A STRING
#-----------------------------------------------------------#
s = "***Python***"
new_s = s.strip("*")
print("After strip('*'):", new_s)
