#WAP TO FIND AREA & PERIMETER OF A TRIANGLE

a,b,c,base,hgt=map(int,input("Enter three sides of Triangle,base,height(seperated by space):-").split())

print("Three sides are :-",a,b,c)
print("Base is :-",base)
print("Height is:-",hgt)

peri=a+b+c
area=1/2*base*hgt

print("The Perimeter of the Triangle is:-",peri)
print("The Area of the Triangle is:-",area)