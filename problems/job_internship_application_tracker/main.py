
import json
import os
from datetime import date


FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "applications.json")

STATUSES = ["Applied", "Interview", "Selected", "Rejected"]


def load_applications():
    """Load saved applications from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            applications = json.load(file)

            if isinstance(applications, list):
                return applications

            print("Invalid application data format.")
            return []

    except (json.JSONDecodeError, OSError):
        print("Unable to read saved applications.")
        return []


def save_applications(applications):
    """Save applications to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(applications, file, indent=4)

        return True

    except OSError:
        print("Error: Unable to save application data.")
        return False


def display_application(application):
    """Display details of a single application."""
    print("\n----------------------------------------")
    print(f"Company       : {application['company']}")
    print(f"Job Role      : {application['role']}")
    print(f"Location      : {application['location']}")
    print(f"Application Date: {application['date']}")
    print(f"Status        : {application['status']}")
    print("----------------------------------------")


def add_application(applications):
    """Add a new job or internship application."""
    print("\n========== ADD NEW APPLICATION ==========")

    company = input("Enter company name: ").strip()
    role = input("Enter job/internship role: ").strip()
    location = input("Enter location: ").strip()

    if not company or not role or not location:
        print("All fields are required.")
        return

    print("\nSelect application status:")

    for index, status in enumerate(STATUSES, start=1):
        print(f"{index}. {status}")

    try:
        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > len(STATUSES):
            print("Invalid status choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    application = {
        "company": company,
        "role": role,
        "location": location,
        "date": str(date.today()),
        "status": STATUSES[choice - 1]
    }

    applications.append(application)

    if save_applications(applications):
        print("\nApplication added successfully!")


def view_applications(applications):
    """Display all saved applications."""
    if not applications:
        print("\nNo applications found.")
        return

    print("\n========== ALL APPLICATIONS ==========")

    for index, application in enumerate(applications, start=1):
        print(f"\nApplication #{index}")
        display_application(application)


def search_application(applications):
    """Search applications by company name."""
    if not applications:
        print("\nNo applications available to search.")
        return

    company_name = input("\nEnter company name to search: ").strip().lower()

    if not company_name:
        print("Company name cannot be empty.")
        return

    found = False

    for application in applications:
        if company_name in application["company"].lower():
            display_application(application)
            found = True

    if not found:
        print("\nNo matching applications found.")


def filter_applications(applications):
    """Filter applications by status."""
    print("\nSelect status to filter:")

    for index, status in enumerate(STATUSES, start=1):
        print(f"{index}. {status}")

    try:
        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > len(STATUSES):
            print("Invalid status choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    selected_status = STATUSES[choice - 1]
    found = False

    for application in applications:
        if application["status"] == selected_status:
            display_application(application)
            found = True

    if not found:
        print(f"\nNo applications with status '{selected_status}' found.")


def update_status(applications):
    """Update the status of an existing application."""
    if not applications:
        print("\nNo applications available to update.")
        return

    view_applications(applications)

    try:
        choice = int(input("\nEnter application number to update: "))

        if choice < 1 or choice > len(applications):
            print("Invalid application number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nSelect new status:")

    for index, status in enumerate(STATUSES, start=1):
        print(f"{index}. {status}")

    try:
        status_choice = int(input("Enter your choice: "))

        if status_choice < 1 or status_choice > len(STATUSES):
            print("Invalid status choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    applications[choice - 1]["status"] = STATUSES[status_choice - 1]

    if save_applications(applications):
        print("\nApplication status updated successfully!")


def show_statistics(applications):
    """Display application statistics."""
    if not applications:
        print("\nNo applications available for statistics.")
        return

    total = len(applications)

    status_count = {}

    for status in STATUSES:
        status_count[status] = 0

    for application in applications:
        status_count[application["status"]] += 1

    print("\n========== APPLICATION STATISTICS ==========")
    print(f"Total Applications : {total}")

    for status, count in status_count.items():
        percentage = (count / total) * 100
        print(f"{status:<12}: {count} ({percentage:.1f}%)")

    print("============================================")


def main():
    applications = load_applications()

    print("=" * 50)
    print("       JOB & INTERNSHIP APPLICATION TRACKER")
    print("=" * 50)

    while True:
        print("\n=============== MAIN MENU ===============")
        print("1. Add new application")
        print("2. View all applications")
        print("3. Search application by company")
        print("4. Filter applications by status")
        print("5. Update application status")
        print("6. View application statistics")
        print("7. Exit")
        print("=========================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_application(applications)

        elif choice == "2":
            view_applications(applications)

        elif choice == "3":
            search_application(applications)

        elif choice == "4":
            filter_applications(applications)

        elif choice == "5":
            update_status(applications)

        elif choice == "6":
            show_statistics(applications)

        elif choice == "7":
            print("\nYour applications are saved.")
            print("Thank you for using the tracker!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()
