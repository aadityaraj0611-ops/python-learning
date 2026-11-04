# College Placement Management System

A menu-driven Python application that manages college placement activities, including student registration, company requirements, eligibility checking, job applications, application status tracking, and placement reports.

## Features

- **Student Registration:** Register students with their names, branches, CGPA, and skills.
- **Student Directory:** Display all registered students and their details.
- **Company Management:** Add companies with minimum CGPA, eligible branches, required skills, and job openings.
- **Eligibility Checker:** Check whether students satisfy company requirements.
- **Job Applications:** Allow eligible students to apply for company openings.
- **Duplicate Application Prevention:** Prevent students from applying to the same company more than once.
- **Application Tracking:** Track applications through Applied, Shortlisted, Selected, and Rejected statuses.
- **Student Search:** Search for students by name.
- **Placement Reports:** Generate application statistics and company-wise placement reports.
- **Opening Management:** Track selected students against available company openings.

## Technologies Used

- Python 3
- Dictionaries and nested dictionaries
- Lists and sets
- Loops
- Conditional statements
- Functions
- String operations
- Exception handling
- Basic arithmetic

## Project Structure

```text
college_placement_management/
│
├── main.py
└── README.md
```

## Application Statuses

| Status | Description |
|---|---|
| Applied | Application successfully submitted |
| Shortlisted | Student shortlisted by the company |
| Selected | Student selected for the position |
| Rejected | Application rejected |

## Eligibility Criteria

A student must satisfy all the following conditions:

1. CGPA must meet the company's minimum requirement.
2. Student's branch must be included in the eligible branches.
3. Student must possess all required skills.

## How to Run

1. Ensure Python 3 is installed.
2. Open the project directory in VS Code.
3. Open the terminal.
4. Run:

```bash
python3 main.py
```

## Sample Placement Report

| Metric | Value |
|---|---:|
| Total Students | 2 |
| Total Companies | 2 |
| Total Applications | 2 |
| Selected | 1 |
| Rejected | 1 |

## Limitations

- Data is stored in memory and resets when the application exits.
- Student and company details cannot currently be edited or deleted.
- Applications are managed within a single program session.
- The system does not connect to actual company recruitment platforms.

## Future Improvements

- Persistent data storage using files or databases.
- Student profile editing and deletion.
- Company profile management.
- Placement analytics and graphical reports.
- Application deadlines and interview scheduling.
- Resume management.
- Export placement reports to CSV.

## Author

Aditya Raj