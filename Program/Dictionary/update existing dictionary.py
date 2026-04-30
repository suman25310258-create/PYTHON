#WAP TO UPDATE MARKS FIELD IN THE EXISTING DICTIONARY

student={
    "Name":'Mohit',
    "Id":101,
    "Roll":8,
    }

val=int(input("Enter the Marks : "))

print("The Initial Dictionary :",student)
student.update({"Marks":val})

print("The Updated Dictionary :",student)