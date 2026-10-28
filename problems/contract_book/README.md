# Contact Book

A beginner-friendly Python application for managing contacts through a terminal-based menu.

## Features

- Add contacts with names and phone numbers.
- Display all saved contacts.
- Search for a contact by name.
- Search without case sensitivity.
- Delete contacts using their displayed numbers.
- Reject empty names and phone numbers.
- Handle invalid menu choices.

## Example

```text
===== Contact Book =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit

Enter your choice: 1
Enter contact name: Rahul
Enter phone number: 9876543210
Contact added successfully!
```

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/contact_book/main.py
```

Follow the menu to add, view, search, or delete contacts.

## Concepts Practiced

- Lists and list indexing
- Functions and parameters
- `while` and `for` loops
- `if`, `elif`, and `else`
- String methods: `strip()` and `lower()`
- List methods: `append()` and `pop()`
- Boolean variables
- Input validation

## Learning Objective

This project demonstrates how Python lists, functions, loops, and conditional statements can be combined to build a simple contact management application.

## Limitations

- Contacts are stored only while the program is running.
- Data is lost when the program exits.
- Contact deletion uses a numeric selection.
- The application does not use a database or permanent storage.