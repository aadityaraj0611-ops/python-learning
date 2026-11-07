# Code Snippet Manager

A Python command-line application that allows developers to store, organize, search, update, and manage reusable code snippets.

## Features

- Add code snippets with titles, programming languages, and descriptions.
- View all saved snippets.
- Search snippets by title or programming language.
- Update existing snippets.
- Delete unwanted snippets.
- View programming languages and the number of snippets stored for each.
- Automatically save snippets using JSON file storage.
- Preserve saved data after restarting the application.
- Validate user inputs and handle invalid entries.

## Technologies Used

- Python 3
- JSON
- `os` module

All modules used are part of Python's standard library.

## Project Structure

```text
code_snippet_manager/
│
├── main.py
├── snippets.json
└── README.md
```

**Note:** `snippets.json` is automatically created when the first snippet is added.

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
   python3 problems/code_snippet_manager/main.py
   ```

## Menu Options

1. Add a snippet
2. View all snippets
3. Search snippets
4. Update a snippet
5. Delete a snippet
6. View programming languages
7. Exit

## Concepts Practiced

- Functions
- Loops and conditional statements
- Lists and dictionaries
- Nested data structures
- Sets
- File handling
- JSON data storage
- Exception handling
- String operations
- Input validation

## Data Storage

The application stores snippets in a local JSON file named `snippets.json`. This allows saved snippets to remain available between program executions.

## Author

Aditya Raj