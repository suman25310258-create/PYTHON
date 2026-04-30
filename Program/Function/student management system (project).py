# WAP TO BUILD A STUDENT MANAGEMENT SYSTEM

students = []   # empty list to store students

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    marks = float(input("Enter Marks: "))
    student = [name, roll, marks]   # store as list
    students.append(student)        # add to list
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No students found!\n")
    else:
        print("\nAll Students:")
        for s in students:
            print(f"Name: {s[0]}, Roll: {s[1]}, Marks: {s[2]}")
        print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s[1] == roll:
            print(f"Found: Name: {s[0]}, Roll: {s[1]}, Marks: {s[2]}\n")
           
    print("❌ Student not found!\n")

def topper():
    if not students:
        print("No students found!\n")
    else:
        top = max(students, key=lambda x: x[2])  # highest marks
        print(f"🏆 Topper: {top[0]} (Roll: {top[1]}) with Marks {top[2]}\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s[1] == roll:
            students.remove(s)
            print("🗑️ Student deleted successfully!\n")
            return
    print("❌ Student not found!\n")

def menu():
    while True:
        print('''\n📘 Student Management System
        1. Add Student
        2. View All Students
        3. Search Student by Roll
        4. Find Topper
        5. Delete Student
        6. Exit''')
        
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            topper()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting... Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()
