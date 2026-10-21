# Simple Calculator

A Python calculator that performs addition, subtraction, multiplication, and division based on the operator entered by the user.

## Features

- Addition using `+`
- Subtraction using `-`
- Multiplication using `*`
- Division using `/`
- Division-by-zero error handling
- Invalid operator handling
- Displays the calculation and its result

## How to Run

Run the following command from the project directory:

```bash
python3 main.py
```

## Example

**Input:**
```text
Enter a number: 10
Enter another number: 5
Enter + for addition
Enter - for subtraction
Enter * for multiplication
Enter / for division
Enter the operator of which you want to do the operation: *
```

**Output:**
```text
The multiplication of 10 and 5 is 50
```

## Error Handling

- If the user chooses `/` and the second number is `0`, the program returns a division-by-zero error message.
- If the user enters an operator other than `+`, `-`, `*`, or `/`, the program displays `Invalid Choice`.

## Python Concepts Practiced

- Variables and data types
- Input and output
- Type conversion using `int()`
- Arithmetic operators
- Functions with parameters and return values
- `if`, `elif`, and `else`
- Nested conditions
- Formatted strings (f-strings)
</EOF>

cat > problems/simple_calculator/README.md <<'EOF'
# Simple Calculator

A beginner-friendly Python calculator that performs four arithmetic operations based on the operator entered by the user.

## Features
- Addition using `+`
- Subtraction using `-`
- Multiplication using `*`
- Division using `/`
- Division-by-zero protection
- Invalid operator handling

## How to Run
Run this command from the project directory:

python3 main.py

## Example

Input:
Enter a number: 10
Enter another number: 5
Enter + for addition
Enter - for subtraction
Enter * for multiplication
Enter / for division
Enter the operator of which you want to do the operation: *

Output:
The multiplication of 10 and 5 is 50

## Error Handling
- If the user chooses `/` and the second number is `0`, the program returns a division-by-zero error message.
- If the user enters an operator other than `+`, `-`, `*`, or `/`, the program displays `Invalid Choice`.

## Python Concepts Practiced
- Variables and data types
- Input and output
- Type conversion using `int()`
- Arithmetic operators
- Functions with parameters and return values
- if/elif/else conditional statements
- Nested conditions
- Formatted strings (f-strings)
