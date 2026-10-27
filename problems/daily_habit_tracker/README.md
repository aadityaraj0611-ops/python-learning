# Daily Habit Tracker

A beginner-friendly Python application for tracking daily habits and measuring completion progress.

## Features

- Starts with three example habits.
- Displays all habits and their completion status.
- Allows users to add new habits.
- Marks habits as completed.
- Prevents a habit from being marked complete twice.
- Calculates the daily completion percentage.
- Validates habit numbers.
- Provides a menu for repeated operations.

## Example

After completing one of three habits, the progress display looks like this:

```text
===== Daily Progress =====
Total habits: 3
Completed habits: 1
Completion percentage: 33.33 %
```

## How to Run

From the root directory of the repository, execute:

```bash
python3 problems/daily_habit_tracker/main.py
```

Use the menu to manage your habits.

## Concepts Practiced

- Lists and list methods such as `append()`
- Functions and parameters
- `while` and `for` loops
- `if`, `elif`, and `else`
- Boolean values
- List indexing
- User input and string methods
- Counters and percentage calculations

## Learning Objective

This project demonstrates how Python lists, functions, loops, and conditional statements can be combined to create a simple habit-tracking application.

## Limitations

- Habits and progress are stored only while the program is running.
- Progress resets when the program exits.
- Habit numbers must be entered as numeric values.
- This version does not track dates or maintain a historical record.