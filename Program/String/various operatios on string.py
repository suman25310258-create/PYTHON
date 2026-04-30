#WAP TO CHANGE CASE OF A STRING
#------------------------------#
s = "pyThon"
print(s.upper())   # All uppercase
print(s.capitalize())  # First letter capital
print(s.lower())   # All lowercase


#WAP TO REPLACE SUBSTRING "is" WITH "was"
#---------------------------------------#
s = "Python is fun."
new_s = s.replace("is", "was")
print(new_s)


#WAP TO CHECK THE STRING STARTS WITH WORD "PYTHON" AND ENDS WITH "FUN"
#--------------------------------------------------------------------#
s = "Python programming is fun"
print(s.startswith("Python"))
print(s.endswith("fun"))


#WAP TO COUNT NUMBER OF WORDS IN A GIVEN STRING
#---------------------------------------------#
s = "Python is fun to learn"
words = s.split()
print("Number of words:", len(words))


#WAP TO CHECK IF A STRING CONTAINS ONLY DIGITS
#--------------------------------------------#
s = "12345"
if s.isdigit():
 print("String contains only digits")
else:
 print("String contains other characters too")
 
  
#WAP TO CHECK IF A STRING CONTAINS ONLY ALPHABETS
#------------------------------------------------# 
s = "HelloWorld"
if s.isalpha():
 print("Contains only alphabets")
else:
 print("Contains other characters too")
 

#WAP TO FIND THE FIRST NON-REPEATING CHARACTER
#--------------------------------------------# 
s = "swiss"
for ch in s:
 if s.count(ch)==1:  #if s.count(ch)<2 :
   print("First non-repeating character:", ch)
   break