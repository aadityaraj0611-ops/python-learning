
# Job & Internship Application Tracker

## Project Overview

The Job & Internship Application Tracker is a Python-based command-line application designed to help users organize and manage their job and internship applications.

It allows users to record application details, track application statuses, search for companies, and view application statistics.

The project uses JSON file handling to store application records permanently, even after the program is closed.

## Features

- **Add Applications:** Record company name, job role, location, application date, and status.
- **View Applications:** Display all saved job and internship applications.
- **Search Applications:** Find applications using company names, including partial matches.
- **Filter by Status:** View applications based on their current status.
- **Update Status:** Change an application's status whenever its progress changes.
- **Application Statistics:** View total applications and status-wise percentages.
- **Persistent Storage:** Save and load application records using a JSON file.
- **Input Validation:** Handle invalid inputs and incorrect menu selections.

## Application Statuses

The tracker supports four application statuses:

1. Applied
2. Interview
3. Selected
4. Rejected

## Technologies Used

- Python 3
- JSON Module
- OS Module
- Datetime Module
- Lists and Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling

## Project Structure

```text
job_internship_application_tracker/
│
├── main.py
├── applications.json
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aadityaraj0611-ops/python-learning.git
```

### 2. Navigate to the project directory

```bash
cd python-learning/problems/job_internship_application_tracker
```

### 3. Run the application

```bash
python3 main.py
```

The application automatically loads previously saved records from `applications.json`.

If the file does not exist, the tracker starts with an empty application list and creates the file when the first application is saved.

## Available Operations

| Option | Operation |
|---|---|
| 1 | Add new application |
| 2 | View all applications |
| 3 | Search application by company |
| 4 | Filter applications by status |
| 5 | Update application status |
| 6 | View application statistics |
| 7 | Exit |

## Data Storage

Application records are stored in JSON format.

Each application contains:

- Company name
- Job or internship role
- Location
- Application date
- Application status

This allows application information to remain available between program executions.

## Learning Outcomes

Through this project, I practiced:

- Reading and writing JSON files.
- Working with lists of dictionaries.
- Organizing programs using functions.
- Searching and filtering records.
- Updating dictionary values.
- Calculating statistics and percentages.
- Handling file-related errors.
- Building a menu-driven management application.

## Future Improvements

- Add application deadlines and interview dates.
- Add reminders for upcoming interviews.
- Export application reports to CSV.
- Add sorting by application date.
- Introduce application notes and contact details.

---

**Author:** Aditya Raj
