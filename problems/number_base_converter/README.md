# Number Base Converter

A beginner-friendly Python project that converts decimal integers into binary, octal, and hexadecimal representations.

## Features

- Converts decimal integers to binary.
- Converts decimal integers to octal.
- Converts decimal integers to hexadecimal.
- Supports zero, positive integers, and negative integers.
- Displays results without Python's base prefixes.

## Example

**Input**
```text
Enter a decimal number: 25
```

**Output**
```text
===== Number Base Converter =====
Decimal: 25
Binary: 11001
Octal: 31
Hexadecimal: 19
```

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/number_base_converter/main.py
```

Enter an integer when prompted.

## Concepts Practiced

- Variables and user input
- Integer type conversion using `int()`
- Built-in functions: `bin()`, `oct()`, and `hex()`
- String slicing
- Conditional expressions
- Handling positive and negative integers

## Learning Objective

This project demonstrates how Python's built-in functions can convert integers between different number bases.

## Limitations

This version accepts integer input only. Entering a decimal fraction or non-numeric text will cause an error.