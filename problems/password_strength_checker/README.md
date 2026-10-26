# Password Strength Checker

A beginner-friendly Python project that evaluates password strength using its length and character variety.

## Features

- Checks password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Detects digits.
- Detects special characters.
- Classifies passwords as Weak, Medium, or Strong.

## Strength Rules

The program awards one point for each condition:

1. Password has at least 8 characters.
2. Password contains an uppercase letter.
3. Password contains a lowercase letter.
4. Password contains a digit.
5. Password contains a special character.

Classification:

- **Weak:** 0–2 points
- **Medium:** 3–4 points
- **Strong:** 5 points

## Example

**Input**
```text
Enter a password: Hello123!
```

**Output**
```text
===== Password Strength Checker =====
Password strength: Strong
```

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/password_strength_checker/main.py
```

Enter a password when prompted.

## Concepts Practiced

- Variables and Boolean values
- `for` loops
- `if`, `elif`, and `else`
- String methods: `isupper()`, `islower()`, and `isdigit()`
- `len()` and string iteration
- Counters and conditional logic

## Learning Objective

This project demonstrates how loops, string methods, and conditional statements can be combined to evaluate user input.

## Limitations

This is an educational exercise, not a complete security assessment. It does not evaluate password predictability, common passwords, or data breaches.