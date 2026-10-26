# Triangle Classifier

A beginner-friendly Python project that checks whether three side lengths form a valid triangle and classifies the triangle by its sides.

## Features

- Accepts three side lengths, including decimal values.
- Rejects zero and negative side lengths.
- Checks the triangle inequality rule.
- Identifies equilateral triangles.
- Identifies isosceles triangles.
- Identifies scalene triangles.

## Triangle Rules

A valid triangle must satisfy all three conditions:

- Side 1 + Side 2 > Side 3
- Side 1 + Side 3 > Side 2
- Side 2 + Side 3 > Side 1

Classification:

- **Equilateral:** All three sides are equal.
- **Isosceles:** Exactly two sides are equal.
- **Scalene:** All three sides are different.

## Example

**Input**
```text
Enter first side: 5
Enter second side: 5
Enter third side: 8
```

**Output**
```text
Valid triangle
Triangle type: Isosceles
```

## How to Run

From the root directory of the repository, execute:

```bash
python3 problems/triangle_classifier/main.py
```

Enter the three side lengths when prompted.

## Concepts Practiced

- Variables and user input
- `float()` type conversion
- `if`, `elif`, and `else`
- Logical operators (`and`, `or`)
- Comparison operators
- Nested conditions
- Mathematical validation

## Learning Objective

This project demonstrates how conditional statements and mathematical rules can be used to validate and classify triangles.

## Limitations

This beginner version expects numeric input. Entering text instead of a number will cause an error.