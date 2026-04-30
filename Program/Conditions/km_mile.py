#WAP TO CONVERT KM TO MILE & VICE-VERSA

print("1.Kilometer to Miles\n"
      "2.Miles to Kilometer")

opt=int(input("\nEnter the operation you want to perform(1/2):- "))

if(opt==1):
 km=int(input("\nEnter the numbers in Kilometers:"))   
 mile=km*0.621371
 print("The",km,"kilometers is =",mile,"miles")

elif(opt==2):
  mile=float(input("\nEnter the numbers in Miles:"))
  km=mile*1.60934
  print("The",mile,"mile is =",km,"kilometers")

else:
  print("Invalid choice")  