# Library Management System

A beginner-friendly Python project that simulates a simple library. Users can view books, borrow available books, and return borrowed books.

## Features

- Displays a list of five books.
- Shows whether each book is available or borrowed.
- Allows users to borrow available books.
- Prevents borrowing a book that is already borrowed.
- Allows users to return borrowed books.
- Prevents returning a book that has not been borrowed.
- Validates book numbers.
- Provides a menu for repeated operations.

## Example

**Borrowing a book**

```text
===== Library Management System =====
1. View Books
2. Borrow Book
3. Return Book
4. Exit

Enter your choice: 2
```

The program displays the book list and asks for the number of the book to borrow.

## How to Run

From the root directory of the repository, execute:

```bash
python3 problems/library_management_system/main.py
```

Follow the menu instructions to manage the books.

## Concepts Practiced

- Lists and list indexing
- Functions and parameters
- `while` and `for` loops
- `if`, `elif`, and `else`
- Boolean values
- User input and output
- Comparison operators
- Updating list elements

## Learning Objective

This project demonstrates how Python lists, functions, loops, and conditional statements can be combined to manage book availability in a simple library system.

## Limitations

- Book records are stored only while the program is running.
- All users share the same book list.
- Book numbers must be entered as numeric values.
- The project does not use a database or permanent storage.