print("Registered Students: Ali, Sahar")

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

student_data = {
    ("Ali", "101"): {
        "Math": 85,
        "Science": 92,
        "English": 75,
        "History": 85,
        "Computer": 88,
    },
    ("Sahar", "102"): {
        "Math": 65,
        "Science": 70,
        "English": 80,
        "History": 95,
        "Computer": 55,
    }
}

key = (name, roll_no)

if key in student_data:
    marks = student_data[key]
    total = sum(marks.values())
    average = total / 5

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print("\n========== STUDENT REPORT CARD =========")
    print(f"Name       : {name}")
    print(f"Roll No.   : {roll_no}")
    print("\nMarks Obtained:")
    for subject, score in marks.items():
        print(f"{subject:<10}: {score}/100")
    print(f"\nTotal Marks: {total}/500")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")
    print("========================================")

else:
    print("\nStudent record not found. Please check your name and roll number.")