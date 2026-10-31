def add_student(students):
    roll = input("Enter student roll number: ")

    if roll in students:
        print("A student with this roll number already exists.")
    else:
        name = input("Enter student name: ")

        students[roll] = {
            "name": name,
            "present": 0,
            "absent": 0
        }
        print("Student added succesffully!")
def mark_attendance(students):
    roll = input("Enter student roll number: ")

    if roll not in students:
        print("Student not found!")
        return

    print("1. Present")
    print("2. Absent")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            students[roll]["absent"] += 1
            print("Attendance marked as PRESENT.")
        elif choice == 2:
            students[roll]["absent"] += 1
            print("Attendance marked as ABSENT.")
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Please enter a valid number.")
def display_students(students):
    if len(students) == 0:
        print("No students registered.")
        return
    print("\n========= STUDENT RECORDS ============")

    for roll, details in students.items():
        total = details["present"] + details["absent"]

        if total > 0:
            percentage = (details["present"] / total) * 100
        else:
            percentage = 0
        print("\nRoll Number:", roll)
        print("Name:", details["name"])
        print("Present:", details["present"])
        print("Absent:", details["absent"])
        print("Attendance:", round(percentage, 2), "%")
def display_low_attendance(students):
    found = False

    print("\n======= STUDENTS BELOW 75% ========")

    for roll, details in students.items():
        total = details["present"] + details["absent"]

        if total > 0:
            percentage = (details["present"] / total) * 100

            if percentage < 75:
                print(details["name"], "-", roll,
                      "-", round(percentage, 2), "%")
                found = True
    if not found:
        print("No students below 75% attendance.")
def main():
    students = {}
    while True:
        print("\n====== ATTENDANCE. MANAGMENT SYSTEM ======")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Display All Students")
        print("4. Students Below 75% Attendace")
        print("5. Total Number of Students")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                add_student(students)
            elif choice == 2:
                mark_attendance(students)
            elif choice == 3:
                display_students(students)
            elif choice == 4:
                display_low_attendance(students)
            elif choice == 5:
                print("Total Students:", len(students))
            elif choice == 6:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Select between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")
main()