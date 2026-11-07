# Password Generator & Security Auditor

A Python-based project that generates secure random passwords and evaluates password strength using basic security checks.

## Features

- Generate secure random passwords using Python's `secrets` module.
- Customize password length (8–128 characters).
- Choose uppercase letters, lowercase letters, numbers, and special characters.
- Generate multiple passwords at once.
- Analyze password strength.
- Identify common passwords and basic password weaknesses.
- Display useful password security tips.
- Validate user inputs.

## Technologies Used

- Python 3
- `secrets`
- `string`

All modules used are part of Python's standard library.

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/aadityaraj0611-ops/python-learning.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-learning
   ```

3. Run the program:

   ```bash
   python3 problems/password_generator_security_auditor/main.py
   ```

## Menu Options

1. Generate a password
2. Generate multiple passwords
3. Check password strength
4. View password security tips
5. Exit

## Concepts Practiced

- Functions
- Loops and conditional statements
- String operations
- Lists
- User input and validation
- Exception handling
- Python standard library modules
- Secure random generation

## Security Note

Generated passwords are not saved to files. The password auditor performs basic local checks and does not guarantee that a password is secure against every attack.

For real accounts, use unique passwords and a trusted password manager.

## Author

Aditya Raj