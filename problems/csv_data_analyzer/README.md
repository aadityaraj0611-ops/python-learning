
# CSV Data Cleaner & Analyzer

## Project Overview

The CSV Data Cleaner & Analyzer is a Python-based command-line application designed to identify data-quality issues, clean CSV datasets, and generate basic statistical reports.

It helps users detect missing values, identify duplicate records, analyze numeric columns, and save cleaned datasets into a separate CSV file.

The project uses Python's built-in CSV module without relying on external libraries such as Pandas.

## Features

- **CSV File Reading:** Read and process structured CSV datasets.
- **Record Display:** Display all records in a readable format.
- **Missing Value Detection:** Identify and count empty cells in each column.
- **Duplicate Detection:** Identify duplicate records in the dataset.
- **Data Cleaning:** Remove duplicate records and replace missing values with `Unknown`.
- **Numeric Analysis:** Calculate minimum, maximum, and average values for numeric columns.
- **Cleaned CSV Export:** Save the cleaned dataset into a separate CSV file.
- **Cleaning Report:** Generate a text report summarizing the cleaning process.
- **Input Validation:** Handle invalid menu selections and file-related errors.

## Technologies Used

- Python 3
- CSV Module
- OS Module
- Lists and Dictionaries
- Sets
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling

## Project Structure

```text
csv_data_analyzer/
│
├── main.py
├── sample_data.csv
├── cleaned_data.csv
├── cleaning_report.txt
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aadityaraj0611-ops/python-learning.git
```

### 2. Navigate to the project directory

```bash
cd python-learning/problems/csv_data_analyzer
```

### 3. Run the application

```bash
python3 main.py
```

## Available Operations

| Option | Operation |
|---|---|
| 1 | Display original CSV records |
| 2 | Detect missing values |
| 3 | Detect duplicate records |
| 4 | Analyze numeric columns |
| 5 | Clean and save CSV data |
| 6 | Generate cleaning report |
| 7 | Exit |

## Sample Dataset

The project includes a sample CSV dataset containing:

- Employee names
- Ages
- Cities
- Salaries
- Departments

The sample dataset intentionally contains missing values and duplicate records to demonstrate the cleaning functionality.

## Data Cleaning Process

The application performs the following operations:

1. Reads the original CSV dataset.
2. Identifies missing values in each column.
3. Detects duplicate records.
4. Removes duplicate records.
5. Replaces missing values with `Unknown`.
6. Saves the cleaned dataset as `cleaned_data.csv`.
7. Generates a summary report in `cleaning_report.txt`.

The original `sample_data.csv` file remains unchanged.

## Learning Outcomes

Through this project, I practiced:

- Reading and writing CSV files using Python.
- Working with lists, dictionaries, and sets.
- Identifying and removing duplicate records.
- Handling missing values.
- Performing basic statistical calculations.
- Organizing code using functions.
- Handling file-related exceptions.
- Building a practical data-cleaning application.

## Future Improvements

- Support user-provided CSV file paths.
- Allow users to select which columns to clean.
- Add more missing-value replacement strategies.
- Support sorting and filtering records.
- Generate graphical data-analysis reports.
- Add additional statistical calculations.

---

**Author:** Aditya Raj
