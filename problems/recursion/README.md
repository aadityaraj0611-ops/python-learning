# Recursive Number Sequence

## Problem Statement

Given a positive integer `N`, print the sequence of numbers from `N` down to `1`, followed by numbers from `1` back up to `N`.

**Constraint:** Solve the problem using recursion without using iterative loops such as `for` or `while`.

## Example

**Input**
```text
4
```

**Output**
```text
4 3 2 1 1 2 3 4
```

## Approach

- If `n == 0`, stop the recursion using a base case.
- Print `n` before the recursive call to display numbers in descending order.
- Call the function with `n - 1`.
- Print `n` after the recursive call returns to display numbers in ascending order.

## Concepts Practiced

- Recursion
- Base cases
- Function calls and returns
- Call stack
