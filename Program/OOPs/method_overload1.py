class Circle:
    def area(self):
        pi=3.14
        r=10
        print("Area of Circle is=", pi*r*r)
        
class Square:
    def area(self,s):
      print("Area of Square is=", s*s)
     
class Rectangle:
    def area(self,length,width):
      print("Area of Rectangle is=", length*width)
     
      
#Create objects
c=Circle()
s=Square()
r=Rectangle()
     
#Call the same method-name on different objects
c.area()
s.area(4)
r.area(5,6)