
name = input("Enter Student Name : ")
roll = input("Enter Roll Number : ")

marks = []
failed = False

print("\nEnter Marks for 5 Subjects (0-100)")
for i in range(1, 6):
    m = float(input(f"Enter marks for Subject {i}: "))
    if m < 0 or m > 100:
        print("Error: Marks should be between 0 and 100")
        exit()
    if m < 40:
        failed = True
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"
        result = "FAIL"

print("\nSTUDENT REPORT CARD")
print(f"Student Name : {name}")
print(f"Roll Number : {roll}")
print(f"Total Marks : {total} / 500.0")
print(f"Percentage : {percentage}%")
print(f"Result : {result}")
print(f"Grade : {grade}")
print(f"Remarks : {remark}")