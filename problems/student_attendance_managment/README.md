# Student Attendance Management System

A menu-driven Python application that helps manage student records and track attendance.

## Features

- Add students using unique roll numbers.
- Prevent duplicate student registration.
- Mark students as present or absent.
- Display all registered students and their attendance records.
- Calculate individual attendance percentages.
- Identify students with attendance below 75%.
- Display the total number of registered students.
- Handle invalid inputs using exception handling.

## Attendance Calculation

Attendance percentage is calculated using:

\[
\text{Attendance Percentage} =
\frac{\text{Present Classes}}{\text{Total Classes}} \times 100
\]

## How to Run

1. Clone this repository.
2. Open the project folder in your terminal.
3. Run:

```bash
python3 problems/student_attendance_management/main.py
```

## Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Functions
- While loops and for loops
- Conditional statements
- User input and type conversion
- Exception handling
- Dictionary methods and built-in functions

## Storage

Student records are stored in memory using dictionaries. Records are reset when the program exits.

## Future Improvements

- Save attendance records permanently.
- Add attendance reports for specific dates.
- Allow editing or deleting student records.

---

**Project Status:** Completed and tested.