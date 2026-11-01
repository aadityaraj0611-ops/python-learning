
employees = {}
next_employee_id = 1001


def add_employee():
    global next_employee_id

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Employee name cannot be empty!")
        return

    department = input("Enter department: ").strip()

    if department == "":
        print("Department cannot be empty!")
        return

    try:
        basic_salary = float(input("Enter basic salary: "))

        if basic_salary <= 0:
            print("Basic salary must be greater than zero!")
            return

        employee_id = next_employee_id
        next_employee_id += 1

        employees[employee_id] = {
            "name": name,
            "department": department,
            "basic_salary": basic_salary,
            "allowances": 0,
            "tax": 0,
            "pf": 0
        }

        print("\nEmployee added successfully!")
        print("Employee ID:", employee_id)

    except ValueError:
        print("Please enter a valid salary!")


def display_employees():
    if len(employees) == 0:
        print("No employees registered!")
        return

    print("\n----- EMPLOYEE DETAILS -----")

    for employee_id, details in employees.items():
        print("\nEmployee ID:", employee_id)
        print("Name:", details["name"])
        print("Department:", details["department"])
        print("Basic Salary: ₹", details["basic_salary"])
        print("Allowances: ₹", details["allowances"])


def search_employee():
    try:
        employee_id = int(input("Enter employee ID: "))

        if employee_id in employees:
            details = employees[employee_id]

            print("\nEmployee Found!")
            print("Employee ID:", employee_id)
            print("Name:", details["name"])
            print("Department:", details["department"])
            print("Basic Salary: ₹", details["basic_salary"])
        else:
            print("Employee does not exist!")

    except ValueError:
        print("Enter a valid employee ID!")


def update_employee():
    try:
        employee_id = int(input("Enter employee ID: "))

        if employee_id not in employees:
            print("Employee does not exist!")
            return

        print("\n1. Update Name")
        print("2. Update Department")
        print("3. Update Basic Salary")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter new name: ").strip()

            if name == "":
                print("Name cannot be empty!")
                return

            employees[employee_id]["name"] = name
            print("Name updated successfully!")

        elif choice == "2":
            department = input("Enter new department: ").strip()

            if department == "":
                print("Department cannot be empty!")
                return

            employees[employee_id]["department"] = department
            print("Department updated successfully!")

        elif choice == "3":
            try:
                salary = float(input("Enter new basic salary: "))

                if salary <= 0:
                    print("Salary must be greater than zero!")
                    return

                employees[employee_id]["basic_salary"] = salary
                print("Basic salary updated successfully!")

            except ValueError:
                print("Enter a valid salary!")

        else:
            print("Invalid choice!")

    except ValueError:
        print("Enter a valid employee ID!")


def calculate_salary(employee_id):
    details = employees[employee_id]

    basic_salary = details["basic_salary"]
    allowances = details["allowances"]
    tax = details["tax"]
    pf = details["pf"]

    gross_salary = basic_salary + allowances
    total_deductions = tax + pf
    net_salary = gross_salary - total_deductions

    return gross_salary, total_deductions, net_salary


def update_salary_components():
    try:
        employee_id = int(input("Enter employee ID: "))

        if employee_id not in employees:
            print("Employee does not exist!")
            return

        print("\n1. Update Allowances")
        print("2. Update Tax")
        print("3. Update Provident Fund (PF)")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = "allowances"
            label = "Allowances"

        elif choice == "2":
            key = "tax"
            label = "Tax"

        elif choice == "3":
            key = "pf"
            label = "Provident Fund"

        else:
            print("Invalid choice!")
            return

        amount = float(input("Enter " + label + " amount: "))

        if amount < 0:
            print("Amount cannot be negative!")
            return

        employees[employee_id][key] = amount

        gross, deductions, net = calculate_salary(employee_id)

        if deductions > gross:
            employees[employee_id][key] = 0
            print("Total deductions cannot exceed gross salary!")
            return

        print(label, "updated successfully!")

    except ValueError:
        print("Please enter valid details!")


def generate_salary_slip():
    try:
        employee_id = int(input("Enter employee ID: "))

        if employee_id not in employees:
            print("Employee does not exist!")
            return

        details = employees[employee_id]

        gross, deductions, net = calculate_salary(employee_id)

        print("\n========== SALARY SLIP ==========")
        print("Employee ID:", employee_id)
        print("Employee Name:", details["name"])
        print("Department:", details["department"])
        print("---------------------------------")
        print("Basic Salary: ₹", details["basic_salary"])
        print("Allowances: ₹", details["allowances"])
        print("---------------------------------")
        print("Gross Salary: ₹", gross)
        print("Tax Deduction: ₹", details["tax"])
        print("PF Deduction: ₹", details["pf"])
        print("Total Deductions: ₹", deductions)
        print("---------------------------------")
        print("NET SALARY: ₹", net)
        print("=================================")

    except ValueError:
        print("Enter a valid employee ID!")


def calculate_total_payroll():
    total_payroll = 0

    if len(employees) == 0:
        print("No employees registered!")
        return

    for employee_id in employees:
        gross, deductions, net = calculate_salary(employee_id)
        total_payroll += net

    print("Total Monthly Payroll: ₹", total_payroll)


def main():
    while True:
        print("\n====== EMPLOYEE PAYROLL MANAGEMENT ======")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee")
        print("4. Update Employee Details")
        print("5. Update Salary Components")
        print("6. Generate Salary Slip")
        print("7. Calculate Total Monthly Payroll")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            update_salary_components()

        elif choice == "6":
            generate_salary_slip()

        elif choice == "7":
            calculate_total_payroll()

        elif choice == "8":
            print("Thank you for using Employee Payroll Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
