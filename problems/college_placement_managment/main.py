
students = {}
companies = {}
applications = {}

next_student_id = 1001
next_company_id = 101
next_application_id = 1


def register_student():
    global next_student_id

    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip()

    try:
        cgpa = float(input("Enter CGPA: "))
    except ValueError:
        print("Invalid CGPA.")
        return

    if name == "" or branch == "":
        print("Name and branch cannot be empty.")
        return

    if cgpa < 0 or cgpa > 10:
        print("CGPA must be between 0 and 10.")
        return

    skills_input = input("Enter skills separated by commas: ").strip()

    if skills_input == "":
        skills = []
    else:
        skills = []

        for skill in skills_input.split(","):
            skill = skill.strip()

            if skill != "" and skill.lower() not in [s.lower() for s in skills]:
                skills.append(skill)

    students[next_student_id] = {
        "name": name,
        "branch": branch,
        "cgpa": cgpa,
        "skills": skills,
        "applications": 0
    }

    print("\nStudent registered successfully!")
    print("Student ID:", next_student_id)

    next_student_id += 1


def display_students():
    if len(students) == 0:
        print("No students registered.")
        return

    print("\n========== STUDENT DIRECTORY ==========")

    for student_id, student in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("CGPA:", student["cgpa"])
        print("Skills:", ", ".join(student["skills"]))
        print("Applications:", student["applications"])


def add_company():
    global next_company_id

    name = input("Enter company name: ").strip()

    if name == "":
        print("Company name cannot be empty.")
        return

    for company in companies.values():
        if company["name"].lower() == name.lower():
            print("Company already exists.")
            return

    try:
        minimum_cgpa = float(input("Enter minimum CGPA requirement: "))
        openings = int(input("Enter number of openings: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if minimum_cgpa < 0 or minimum_cgpa > 10:
        print("Minimum CGPA must be between 0 and 10.")
        return

    if openings <= 0:
        print("Openings must be greater than zero.")
        return

    eligible_branches_input = input(
        "Enter eligible branches separated by commas: "
    ).strip()

    eligible_branches = []

    if eligible_branches_input == "":
        print("At least one eligible branch is required.")
        return

    for branch in eligible_branches_input.split(","):
        branch = branch.strip()

        if branch != "" and branch.lower() not in [
            b.lower() for b in eligible_branches
        ]:
            eligible_branches.append(branch)

    if len(eligible_branches) == 0:
        print("At least one eligible branch is required.")
        return

    required_skills_input = input(
        "Enter required skills separated by commas (or leave blank): "
    ).strip()

    required_skills = []

    if required_skills_input != "":
        for skill in required_skills_input.split(","):
            skill = skill.strip()

            if skill != "" and skill.lower() not in [
                s.lower() for s in required_skills
            ]:
                required_skills.append(skill)

    companies[next_company_id] = {
        "name": name,
        "minimum_cgpa": minimum_cgpa,
        "openings": openings,
        "eligible_branches": eligible_branches,
        "required_skills": required_skills,
        "applications": 0,
        "selected": 0
    }

    print("\nCompany added successfully!")
    print("Company ID:", next_company_id)

    next_company_id += 1


def display_companies():
    if len(companies) == 0:
        print("No companies registered.")
        return

    print("\n========== COMPANY DIRECTORY ==========")

    for company_id, company in companies.items():
        print("\nCompany ID:", company_id)
        print("Name:", company["name"])
        print("Minimum CGPA:", company["minimum_cgpa"])
        print("Openings:", company["openings"])
        print("Eligible Branches:", ", ".join(company["eligible_branches"]))
        print("Required Skills:", ", ".join(company["required_skills"]))
        print("Applications:", company["applications"])
        print("Selected Students:", company["selected"])


def check_eligibility(student_id, company_id):
    student = students[student_id]
    company = companies[company_id]

    if student["cgpa"] < company["minimum_cgpa"]:
        return False, "CGPA requirement not satisfied."

    branch_eligible = False

    for branch in company["eligible_branches"]:
        if student["branch"].lower() == branch.lower():
            branch_eligible = True
            break

    if not branch_eligible:
        return False, "Your branch is not eligible."

    for required_skill in company["required_skills"]:
        skill_found = False

        for student_skill in student["skills"]:
            if required_skill.lower() == student_skill.lower():
                skill_found = True
                break

        if not skill_found:
            return False, "Missing required skill: " + required_skill

    return True, "Student is eligible."


def check_student_eligibility():
    if len(students) == 0 or len(companies) == 0:
        print("Students and companies must be registered first.")
        return

    try:
        student_id = int(input("Enter student ID: "))
        company_id = int(input("Enter company ID: "))
    except ValueError:
        print("Please enter valid IDs.")
        return

    if student_id not in students:
        print("Student not found.")
        return

    if company_id not in companies:
        print("Company not found.")
        return

    eligible, message = check_eligibility(student_id, company_id)

    print("\nEligibility Result:", message)


def apply_for_company():
    global next_application_id

    try:
        student_id = int(input("Enter student ID: "))
        company_id = int(input("Enter company ID: "))
    except ValueError:
        print("Please enter valid IDs.")
        return

    if student_id not in students:
        print("Student not found.")
        return

    if company_id not in companies:
        print("Company not found.")
        return

    eligible, message = check_eligibility(student_id, company_id)

    if not eligible:
        print("Application rejected:", message)
        return

    company = companies[company_id]

    if company["openings"] <= 0:
        print("No openings available.")
        return

    for application in applications.values():
        if (
            application["student_id"] == student_id
            and application["company_id"] == company_id
        ):
            print("Student has already applied to this company.")
            return

    applications[next_application_id] = {
        "student_id": student_id,
        "company_id": company_id,
        "status": "Applied"
    }

    students[student_id]["applications"] += 1
    company["applications"] += 1

    print("\nApplication submitted successfully!")
    print("Application ID:", next_application_id)
    print("Student:", students[student_id]["name"])
    print("Company:", company["name"])
    print("Status: Applied")

    next_application_id += 1


def update_application_status():
    if len(applications) == 0:
        print("No applications available.")
        return

    try:
        application_id = int(input("Enter application ID: "))
    except ValueError:
        print("Invalid application ID.")
        return

    if application_id not in applications:
        print("Application not found.")
        return

    application = applications[application_id]

    if application["status"] in ["Selected", "Rejected"]:
        print("This application has already been finalized.")
        return

    print("\n1. Shortlisted")
    print("2. Selected")
    print("3. Rejected")

    choice = input("Choose new application status: ")

    if choice == "1":
        application["status"] = "Shortlisted"

    elif choice == "2":
        company = companies[application["company_id"]]

        if company["selected"] >= company["openings"]:
            print("All available openings have been filled.")
            return

        application["status"] = "Selected"
        company["selected"] += 1

    elif choice == "3":
        application["status"] = "Rejected"

    else:
        print("Invalid status choice.")
        return

    print("Application status updated successfully!")
    print("New Status:", application["status"])


def display_applications():
    if len(applications) == 0:
        print("No applications available.")
        return

    print("\n========== APPLICATION HISTORY ==========")

    for application_id, application in applications.items():
        student = students[application["student_id"]]
        company = companies[application["company_id"]]

        print("\nApplication ID:", application_id)
        print("Student:", student["name"])
        print("Company:", company["name"])
        print("Status:", application["status"])


def search_student():
    if len(students) == 0:
        print("No students registered.")
        return

    search_name = input("Enter student name to search: ").strip().lower()
    found = False

    for student_id, student in students.items():
        if search_name in student["name"].lower():
            print("\nStudent ID:", student_id)
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("CGPA:", student["cgpa"])
            print("Skills:", ", ".join(student["skills"]))
            found = True

    if not found:
        print("Student not found.")


def placement_report():
    total_applications = len(applications)
    shortlisted = 0
    selected = 0
    rejected = 0
    applied = 0

    for application in applications.values():
        if application["status"] == "Applied":
            applied += 1
        elif application["status"] == "Shortlisted":
            shortlisted += 1
        elif application["status"] == "Selected":
            selected += 1
        elif application["status"] == "Rejected":
            rejected += 1

    print("\n========== PLACEMENT REPORT ==========")
    print("Total Students:", len(students))
    print("Total Companies:", len(companies))
    print("Total Applications:", total_applications)
    print("Applied:", applied)
    print("Shortlisted:", shortlisted)
    print("Selected:", selected)
    print("Rejected:", rejected)

    print("\n========== COMPANY-WISE REPORT ==========")

    for company_id, company in companies.items():
        print("\nCompany:", company["name"])
        print("Total Applications:", company["applications"])
        print("Selected Students:", company["selected"])
        print("Remaining Openings:", company["openings"] - company["selected"])


def main():
    while True:
        print("\n========== COLLEGE PLACEMENT MANAGEMENT SYSTEM ==========")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Add Company")
        print("4. Display Companies")
        print("5. Check Student Eligibility")
        print("6. Apply for Company")
        print("7. Update Application Status")
        print("8. Display Application History")
        print("9. Search Student")
        print("10. Placement Report")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            add_company()

        elif choice == "4":
            display_companies()

        elif choice == "5":
            check_student_eligibility()

        elif choice == "6":
            apply_for_company()

        elif choice == "7":
            update_application_status()

        elif choice == "8":
            display_applications()

        elif choice == "9":
            search_student()

        elif choice == "10":
            placement_report()

        elif choice == "11":
            print("Thank you for using College Placement Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
