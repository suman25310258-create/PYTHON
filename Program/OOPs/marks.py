class Student:
    def __init__(self, name, marks):  
        self.name = name
        self.marks = marks

student1 = Student('Suman', 70)
student2 = Student('Ratna', 80)

print(student1.name, student1.marks)
print(student2.name, student2.marks)
