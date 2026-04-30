#WAP TO CHECK IF A GIVEN KEY EXISTS IN A DICTIONARY OR NOT

d={"Mohit":"Executive","Dipankar":"Engineer","Toton":"Developer"}

p=input("Enter the key you want to check : ")

if p in d:
 print("The Key is present.")
 print("The value against the key is : ",d[p])
else:
 print("The Key is not present.")   