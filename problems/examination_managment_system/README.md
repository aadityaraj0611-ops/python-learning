# Examination Management System

A menu-driven Examination Management System developed using Python. This project simulates academic examination operations, including student registration, subject management, examination creation, marks entry, automatic grade calculation, report card generation, class performance analysis, and student rankings.

## Features

### 1. Student Management
- Register new students with unique student IDs.
- Display all registered students.
- Search students using their IDs.
- Validate student information and semester numbers.

### 2. Subject Management
- Add new subjects.
- Assign maximum marks to each subject.
- Display all available subjects.
- Validate subject details and maximum marks.

### 3. Examination Management
- Create examinations for registered subjects.
- Assign unique examination IDs.
- Display examination details.
- Validate subject IDs and examination names.

### 4. Marks Management
- Enter marks for registered students.
- Associate marks with specific examinations.
- Prevent duplicate marks entry.
- Validate marks against maximum marks.

### 5. Automatic Grade Calculation

Grades are calculated using the student's percentage.

| Percentage | Grade |
|---|---|
| 90% and above | A+ |
| 80%–89.99% | A |
| 70%–79.99% | B |
| 60%–69.99% | C |
| 50%–59.99% | D |
| 40%–49.99% | E |
| Below 40% | F |

Students scoring at least 40% pass an examination.

### 6. Student Report Cards
- Generate individual student report cards.
- Display subject-wise examination results.
- Calculate total marks and overall percentage.
- Display overall pass or fail status.

### 7. Class Performance Analysis
- Calculate class average percentage.
- Identify the highest-performing student.
- Display the highest percentage.

### 8. Student Rankings
- Rank students based on their overall percentages.
- Display student names, IDs, and percentages.
- Sort rankings in descending order.

## Technologies Used

- Python 3
- Dictionaries and nested dictionaries
- Lists
- Loops
- Conditional statements
- Functions
- Exception handling
- Lambda functions
- Built-in sorting

## Important Formulas

**Percentage:**

Percentage = (Marks Obtained / Maximum Marks) × 100

**Overall Percentage:**

Overall Percentage = (Total Marks Obtained / Total Maximum Marks) × 100

**Class Average:**

Class Average = Sum of Individual Student Percentages / Number of Students with Results

## How to Run

Open the project directory in your terminal and execute:

```bash
python3 main.py
```

## Testing

The application was tested using 45 test cases covering:

- Student registration and validation
- Student searching
- Subject creation
- Examination creation
- Marks entry and validation
- Duplicate marks prevention
- Automatic grade calculation
- Individual report card generation
- Class performance analysis
- Student rankings
- Invalid inputs and nonexistent records

**All 45 test cases passed.**

## Current Limitations

- Data is stored in memory and resets when the program exits.
- There is no permanent database or file storage.
- Students are compared using the examinations for which they have recorded marks.
- The system does not enforce that every student must attempt the same examinations.
- There is no authentication or administrator login system.

## Future Improvements

- Add permanent data storage using files or a database.
- Add examination schedules and examination dates.
- Implement subject-wise and semester-wise rankings.
- Add attendance-based eligibility.
- Generate downloadable student report cards.
- Introduce administrator and student login systems.
- Handle ranking ties using competition ranking.

## Project Status

**Completed — all 45 test cases passed.**