#WAP TO COUNT LOWER,UPPER,DIGIT,SPECIAL-SYMBOL IN A STRING

stn="@123Abc!"
low_count=0
upp_count=0
digi_count=0
spcl_count=0

for i in stn:
 if i.islower():
  low_count=low_count+1
 elif  i.isupper():
  upp_count=upp_count+1
 elif i.isdigit():
  digi_count=digi_count+1
 else:
  spcl_count=spcl_count+1
  
print("Lower Count :",low_count)
print("Upper Count :",upp_count)     
print("Digit Count :",digi_count)
print("Special Character :",spcl_count)