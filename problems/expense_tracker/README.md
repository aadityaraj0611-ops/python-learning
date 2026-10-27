# Expense Tracker

A beginner-friendly Python project for recording expenses, tracking total spending, and managing a budget.

## Features

- Set an initial budget.
- Add multiple expenses.
- View all recorded expenses.
- Calculate total spending.
- Check the remaining budget.
- Warn when spending exceeds the budget.
- Reject zero or negative expense amounts.
- Handle invalid menu choices.

## Example

**Input**
```text
Enter your total budget: 2000
```

After adding expenses of ₹150 and ₹250, the program displays:

```text
Total spending: ₹ 400.0
Budget: ₹ 2000.0
Total spending: ₹ 400.0
Remaining budget: ₹ 1600.0
```

## How to Run

From the root directory of the repository, execute:

```bash
python3 problems/expense_tracker/main.py
```

Enter your budget and use the menu to manage expenses.

## Concepts Practiced

- Variables and user input
- Lists and the `append()` method
- Functions and parameters
- `while` and `for` loops
- `if`, `elif`, and `else`
- Arithmetic and comparison operators
- `len()` and `range()`
- Rounding numbers using `round()`

## Learning Objective

This project demonstrates how Python lists, loops, functions, and conditional statements can work together to build a simple budget-tracking application.

## Limitations

- Expenses are stored only while the program is running.
- Data is lost when the program exits.
- The current version expects numeric input for budgets and expense amounts.
- This is an educational project, not a financial management service.