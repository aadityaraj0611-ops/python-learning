def add_contact(names, numbers):
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()

    if name == "" or number == "":
        print("Name and phone number cannot be empty.")
    else:
        names.append(name)
        numbers.append(number)
        print("Contact added successfully!")

def view_contacts(names, numbers):
    print("\n===== All Contacts =====")

    if len(names) == 0:
        print("No contacts found.")
    else:
        for i in range(len(names)):
            print(i + 1, ".", names[i], "-", numbers[i])

def search_contacts(names, numbers):
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    for i in range(len(names)):
        if names[i].lower() == search_name:
            print("Contact found: ", names[i], "-", numbers[i])
            found = True

    if not found:
        print("Contact not found.")

def delete_contacts(names, numbers):
    view_contacts(names, numbers)

    if len(names) == 0:
        return

    choice = int(input("Enter contact number to delete: "))

    if choice < 1 or choice > len(names):
        print("Invalid contact number.")
    else:
        deleted_name = names.pop(choice - 1)
        numbers.pop(choice - 1)
        print("Contact deleted: ", deleted_name)

names = []
numbers = []

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter yout choice: ")

    if choice == "1":
        add_contact(names, numbers)
    elif choice == "2":
        view_contacts(names, numbers)
    elif choice == "3":
        search_contacts(names,numbers)
    elif choice == "4":
        delete_contacts(names, numbers)
    elif choice == "5":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Inavlid choice. Please select 1-5.")