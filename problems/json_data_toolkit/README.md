# JSON Data Toolkit

A Python command-line application that helps developers validate, format, minify, view, compare, and search JSON files.

## Features

- **JSON Validator:** Check whether a JSON file contains valid JSON syntax.
- **JSON Formatter:** Convert JSON into properly indented and readable format.
- **JSON Minifier:** Remove unnecessary whitespace from JSON files.
- **JSON Viewer:** Display JSON data in a structured and readable format.
- **JSON Comparator:** Compare two JSON files and identify whether their data is identical.
- **JSON Key Finder:** Search for keys inside nested JSON objects and lists.
- **Error Handling:** Handle missing files, invalid JSON syntax, and incorrect inputs.

## Technologies Used

- Python 3
- `json` module
- `os` module

All modules used are part of Python's standard library. No external packages are required.

## Project Structure

```text
json_data_toolkit/
│
├── main.py
├── sample.json
├── sample2.json
├── different.json
├── invalid.json
├── sample_formatted.json
├── sample_minified.json
└── README.md
```

**Note:** The formatted and minified files are generated automatically by the application. The other JSON files are sample files used for testing.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/aadityaraj0611-ops/python-learning.git
   ```

2. Navigate to the repository:

   ```bash
   cd python-learning
   ```

3. Run the application:

   ```bash
   python3 problems/json_data_toolkit/main.py
   ```

## Menu Options

1. Validate JSON file
2. Format JSON file
3. Minify JSON file
4. View JSON data
5. Compare two JSON files
6. Find a JSON key
7. Exit

## Example

**Sample JSON Input:**

```json
{
    "name": "Aditya",
    "age": 19,
    "education": {
        "year": 1,
        "branch": "CSE"
    }
}
```

**Nested Key Search:**

Searching for the key `year` returns:

```text
Path: education.year
Value: 1
Total matches: 1
```

## Concepts Practiced

- Functions
- Loops and conditional statements
- Lists and dictionaries
- Nested dictionaries and lists
- File handling
- JSON parsing and serialization
- Exception handling
- String operations
- Recursive data searching
- Input validation
- Python standard library modules

## Limitations

This project provides basic JSON file management functionality. It does not currently support visual JSON editing or schema validation.

## Author

Aditya Raj