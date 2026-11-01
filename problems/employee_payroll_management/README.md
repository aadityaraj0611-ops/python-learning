# Employee Payroll Management System

## Project Overview

The Employee Payroll Management System is a menu-driven Python application designed to manage employee records and calculate monthly salaries.

It allows users to add employees, search and update employee information, manage salary components, generate salary slips, and calculate the total monthly payroll.

## Features

1. **Add Employee** – Register employees with unique employee IDs.
2. **Display Employees** – View all registered employees and their details.
3. **Search Employee** – Find an employee using their employee ID.
4. **Update Employee Details** – Update employee names, departments, and basic salaries.
5. **Manage Salary Components** – Update allowances, tax, and provident fund deductions.
6. **Calculate Gross Salary** – Calculate basic salary plus allowances.
7. **Calculate Net Salary** – Subtract total deductions from gross salary.
8. **Generate Salary Slip** – Display an individual employee's salary breakdown.
9. **Calculate Total Payroll** – Calculate the combined net salary of all employees.
10. **Input Validation** – Handle invalid inputs, negative amounts, and excessive deductions.

## Salary Calculation

The application follows these formulas:

**Gross Salary**

Gross Salary = Basic Salary + Allowances

**Total Deductions**

Total Deductions = Tax + Provident Fund

**Net Salary**

Net Salary = Gross Salary - Total Deductions

## Technologies Used

- Python 3
- Visual Studio Code
- Terminal

## How to Run

1. Open the project folder in VS Code.
2. Open the Terminal.
3. Navigate to the project directory.
4. Execute:

```bash
python3 main.py
```

## Python Concepts Used

- Variables and data types
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions
- Dictionaries and nested dictionaries
- Lists
- Dictionary methods
- Exception handling (`try`, `except`)
- Arithmetic operations
- User input and output

## Data Storage

Employee records are stored in Python dictionaries during program execution.

**Note:** The application currently uses temporary in-memory storage. Employee information is lost when the program is closed.

## Testing

The application was tested for:

- Employee creation and searching
- Displaying employee records
- Updating employee information
- Updating salary components
- Gross and net salary calculations
- Salary slip generation
- Total monthly payroll calculation
- Negative amount validation
- Excessive deduction prevention
- Invalid employee ID and menu input handling

All 18 test cases were completed successfully.

## Future Improvements

- Permanent employee data storage using file handling.
- Employee deletion functionality.
- PIN-based administrator login.
- Automatic salary calculations using configurable deduction rates.
- Salary slip generation as downloadable PDF files.
- Employee attendance and bonus management.

## Project Status

Completed
