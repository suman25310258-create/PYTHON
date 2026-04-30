#WAP IF A SUBSTRING EXISTS IN A GIVEN STRING (without using in keyword)
#----------------------------------------------------------------------#

s = "Python programming is fun"
sub = "programming"

if s.find(sub) != -1:
    print("Substring found!")
else:
    print("Substring not found.")
