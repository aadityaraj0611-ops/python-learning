# Square of Rectangles

## Problem Statement

Aryan loves squares but dislikes rectangles. He is given three rectangles with dimensions `l1 × b1`, `l2 × b2`, and `l3 × b3`.

Determine whether the three rectangles can be arranged to form a perfect square, subject to these rules:

- The rectangles must not overlap.
- Their edges must be aligned.
- Rotation is not allowed.
- The dimensions satisfy `l3 <= l2 <= l1` and `b3 <= b2 <= b1`.

Return `"YES"` if the rectangles can form a square; otherwise, return `"NO"`.

## Approach

The solution checks specific dimension relationships using conditional statements to determine whether the rectangles can fit together to form a square.

## Python Concepts Practiced

- Functions and return values
- Conditional statements (`if`)
- Comparison operators
- Arithmetic and logical reasoning

## Example

**Input dimensions**
```text
5 3
5 1
5 1
```

**Expected output**
```text
YES
```

## Key Learning

This problem develops logical reasoning and the ability to translate geometric constraints into Python conditions.
