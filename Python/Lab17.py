

def calculate_results(marks):
    """Receives a list of marks, calculates and returns total and average"""
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    """Receives roll number and student dictionary, prints formatted line"""
    total, average = calculate_results(student["marks"])
    print(f"Roll No: {roll} | Name: {student['name']} | Marks: {student['marks']} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    """Checks if roll already exists, if yes shows error, otherwise adds"""
    if roll in records:
        print(f"[ERROR] Student with Roll No {roll} already exists!")
    else:
        records[roll] = {"name": name, "marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


students = {
    "101": {"name": "Aman", "marks": [85, 90, 78]},
    "102": {"name": "Riya", "marks": [92, 88, 95]},
    "103": {"name": "Karan", "marks": [74, 80, 82]}
}

while True:
    print("\n" + "="*50)
    print("      STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*50)
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    
    if choice == '1':
        print("\n--- All Student Records ---")
        for roll, data in students.items():
            display_student(roll, data)
        print(f"Total Students: {len(students)}")

    
    elif choice == '2':
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        print("Enter marks for 3 subjects:")
        marks = []
        for i in range(1, 4):
            m = int(input(f"Subject {i}: "))
            marks.append(m)
        add_student(students, roll, name, marks)

    
    elif choice == '3':
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student:
            print("\n[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    
    elif choice == '4':
        print("\nThank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")