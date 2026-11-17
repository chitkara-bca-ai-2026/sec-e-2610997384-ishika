

students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
}

while True:
    print("\n" + "="*45)
    print("  STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("="*45)
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    
    if choice == '1':
        print("\n--- Enrolled Student Records ---")
        for roll, data in students.items():
            print(f"Roll No: {roll} | Name: {data['Name']} | Branch: {data['Branch']} | Sem: {data['Semester']} | Marks: {data['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    
    elif choice == '2':
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"Name      : {student['Name']}")
            print(f"Branch    : {student['Branch']}")
            print(f"Semester  : {student['Semester']}")
            print(f"Marks     : {student['Marks']}")
        else:
            print(f"Student with Roll No {roll} not found!")

    
    elif choice == '3':
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"Roll No {roll} already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            marks = []
            for i in range(1, 4):
                m = int(input(f"Subject {i}: "))
                marks.append(m)
            students[roll] = {"Name": name, "Branch": branch, "Semester": sem, "Marks": marks}
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    
    elif choice == '4':
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            print(f"Current details for {students[roll]['Name']} (Roll {roll}):")
            print(f"1. Branch: {students[roll]['Branch']} | 2. Semester: {students[roll]['Semester']}")
            field = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if field == '1':
                new_branch = input("Enter new Branch: ")
                students[roll]['Branch'] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field == '2':
                new_sem = input("Enter new Semester: ")
                students[roll]['Semester'] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("Invalid field choice!")
        else:
            print(f"Student with Roll No {roll} not found!")

    
    elif choice == '5':
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        if student:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            result = "PASS" if average >= 40 else "FAIL"
            print("\n" + "="*50)
            print("                ACADEMIC REPORT")
            print("="*50)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result}")
            print("="*50)
        else:
            print(f"Student with Roll No {roll} not found!")


    elif choice == '6':
        roll = input("Enter Roll Number to delete: ")
        deleted = students.pop(roll, None)
        if deleted:
            print(f"\n[SUCCESS] Record for '{deleted['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"Student with Roll No {roll} not found!")


    elif choice == '7':
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")

  