
students = {}
subjects = {}
exams = {}
results = {}

next_student_id = 1001
next_subject_id = 101
next_exam_id = 1


def register_student():
    global next_student_id

    print("\n--- Student Registration ---")

    name = input("Enter student name: ").strip()
    branch = input("Enter student branch: ").strip()
    semester = input("Enter semester: ").strip()

    if name == "" or branch == "" or semester == "":
        print("All student details are required.")
        return

    try:
        semester = int(semester)

        if semester < 1 or semester > 12:
            print("Semester must be between 1 and 12.")
            return

    except ValueError:
        print("Semester must be a valid number.")
        return

    student_id = next_student_id

    students[student_id] = {
        "name": name,
        "branch": branch,
        "semester": semester
    }

    next_student_id += 1

    print("Student registered successfully!")
    print("Student ID:", student_id)


def display_students():
    print("\n--- Registered Students ---")

    if len(students) == 0:
        print("No students registered.")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Branch:", details["branch"])
        print("Semester:", details["semester"])


def search_student():
    print("\n--- Search Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        if student_id in students:
            details = students[student_id]

            print("Student Name:", details["name"])
            print("Branch:", details["branch"])
            print("Semester:", details["semester"])
        else:
            print("Student does not exist.")

    except ValueError:
        print("Please enter a valid student ID.")


def add_subject():
    global next_subject_id

    print("\n--- Add Subject ---")

    subject_name = input("Enter subject name: ").strip()

    if subject_name == "":
        print("Subject name cannot be empty.")
        return

    try:
        max_marks = float(input("Enter maximum marks: "))

        if max_marks <= 0:
            print("Maximum marks must be positive.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    subject_id = next_subject_id

    subjects[subject_id] = {
        "name": subject_name,
        "max_marks": max_marks
    }

    next_subject_id += 1

    print("Subject added successfully!")
    print("Subject ID:", subject_id)


def display_subjects():
    print("\n--- Available Subjects ---")

    if len(subjects) == 0:
        print("No subjects available.")
        return

    for subject_id, details in subjects.items():
        print("\nSubject ID:", subject_id)
        print("Subject Name:", details["name"])
        print("Maximum Marks:", details["max_marks"])


def create_exam():
    global next_exam_id

    print("\n--- Create Examination ---")

    if len(subjects) == 0:
        print("Please add subjects before creating an exam.")
        return

    try:
        subject_id = int(input("Enter subject ID: "))

        if subject_id not in subjects:
            print("Subject does not exist.")
            return

        exam_name = input("Enter examination name: ").strip()

        if exam_name == "":
            print("Examination name cannot be empty.")
            return

        exam_id = next_exam_id

        exams[exam_id] = {
            "name": exam_name,
            "subject_id": subject_id
        }

        next_exam_id += 1

        print("Examination created successfully!")
        print("Exam ID:", exam_id)

    except ValueError:
        print("Please enter a valid subject ID.")


def display_exams():
    print("\n--- Examination Records ---")

    if len(exams) == 0:
        print("No examinations created.")
        return

    for exam_id, details in exams.items():
        subject_id = details["subject_id"]

        print("\nExam ID:", exam_id)
        print("Exam Name:", details["name"])
        print("Subject:", subjects[subject_id]["name"])
        print("Maximum Marks:", subjects[subject_id]["max_marks"])


def enter_marks():
    print("\n--- Enter Student Marks ---")

    if len(students) == 0 or len(exams) == 0:
        print("Register students and create examinations first.")
        return

    try:
        student_id = int(input("Enter student ID: "))

        if student_id not in students:
            print("Student does not exist.")
            return

        exam_id = int(input("Enter exam ID: "))

        if exam_id not in exams:
            print("Examination does not exist.")
            return

        subject_id = exams[exam_id]["subject_id"]
        max_marks = subjects[subject_id]["max_marks"]

        if student_id not in results:
            results[student_id] = {}

        if exam_id in results[student_id]:
            print("Marks have already been entered for this student and exam.")
            return

        marks = float(input("Enter marks obtained: "))

        if marks < 0 or marks > max_marks:
            print("Marks must be between 0 and", max_marks)
            return

        percentage = (marks / max_marks) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        status = "Pass" if percentage >= 40 else "Fail"

        results[student_id][exam_id] = {
            "marks": marks,
            "percentage": percentage,
            "grade": grade,
            "status": status
        }

        print("Marks entered successfully!")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("Result:", status)

    except ValueError:
        print("Please enter valid numeric values.")


def generate_report_card():
    print("\n--- Student Report Card ---")

    try:
        student_id = int(input("Enter student ID: "))

        if student_id not in students:
            print("Student does not exist.")
            return

        print("\nStudent Name:", students[student_id]["name"])
        print("Student ID:", student_id)
        print("Branch:", students[student_id]["branch"])
        print("Semester:", students[student_id]["semester"])

        if student_id not in results or len(results[student_id]) == 0:
            print("No examination results available.")
            return

        total_marks = 0
        total_max_marks = 0
        failed = False

        print("\n--- Examination Results ---")

        for exam_id, result in results[student_id].items():
            exam = exams[exam_id]
            subject_id = exam["subject_id"]
            subject = subjects[subject_id]

            print("\nExam:", exam["name"])
            print("Subject:", subject["name"])
            print("Marks:", result["marks"], "/", subject["max_marks"])
            print("Percentage:", round(result["percentage"], 2), "%")
            print("Grade:", result["grade"])
            print("Status:", result["status"])

            total_marks += result["marks"]
            total_max_marks += subject["max_marks"]

            if result["status"] == "Fail":
                failed = True

        overall_percentage = (total_marks / total_max_marks) * 100

        print("\nTotal Marks:", total_marks, "/", total_max_marks)
        print("Overall Percentage:", round(overall_percentage, 2), "%")

        if failed:
            print("Overall Result: Fail")
        else:
            print("Overall Result: Pass")

    except ValueError:
        print("Please enter a valid student ID.")


def class_performance():
    print("\n--- Class Performance Report ---")

    if len(results) == 0:
        print("No examination results available.")
        return

    total_percentage = 0
    student_count = 0
    highest_percentage = -1
    highest_student = ""

    for student_id, student_results in results.items():
        if len(student_results) == 0:
            continue

        total_marks = 0
        total_max_marks = 0

        for exam_id, result in student_results.items():
            subject_id = exams[exam_id]["subject_id"]

            total_marks += result["marks"]
            total_max_marks += subjects[subject_id]["max_marks"]

        percentage = (total_marks / total_max_marks) * 100

        total_percentage += percentage
        student_count += 1

        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_student = students[student_id]["name"]

    if student_count == 0:
        print("No valid results available.")
        return

    average = total_percentage / student_count

    print("Number of students with results:", student_count)
    print("Class Average:", round(average, 2), "%")
    print("Highest Percentage:", round(highest_percentage, 2), "%")
    print("Top Performing Student:", highest_student)


def student_rankings():
    print("\n--- Student Rankings ---")

    ranking_data = []

    for student_id, student_results in results.items():
        if len(student_results) == 0:
            continue

        total_marks = 0
        total_max_marks = 0

        for exam_id, result in student_results.items():
            subject_id = exams[exam_id]["subject_id"]

            total_marks += result["marks"]
            total_max_marks += subjects[subject_id]["max_marks"]

        percentage = (total_marks / total_max_marks) * 100

        ranking_data.append({
            "student_id": student_id,
            "name": students[student_id]["name"],
            "percentage": percentage
        })

    if len(ranking_data) == 0:
        print("No student results available.")
        return

    ranking_data.sort(
        key=lambda student: student["percentage"],
        reverse=True
    )

    rank = 1

    for student in ranking_data:
        print(
            rank,
            ".",
            student["name"],
            "| ID:",
            student["student_id"],
            "| Percentage:",
            round(student["percentage"], 2), "%"
        )

        rank += 1


def main():
    while True:
        print("\n========== EXAMINATION MANAGEMENT SYSTEM ==========")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Add Subject")
        print("5. Display Subjects")
        print("6. Create Examination")
        print("7. Display Examinations")
        print("8. Enter Student Marks")
        print("9. Generate Student Report Card")
        print("10. Class Performance Report")
        print("11. Student Rankings")
        print("12. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            add_subject()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            create_exam()
        elif choice == "7":
            display_exams()
        elif choice == "8":
            enter_marks()
        elif choice == "9":
            generate_report_card()
        elif choice == "10":
            class_performance()
        elif choice == "11":
            student_rankings()
        elif choice == "12":
            print("Thank you for using the Examination Management System!")
            break
        else:
            print("Invalid choice. Please select between 1 and 12.")


main()
