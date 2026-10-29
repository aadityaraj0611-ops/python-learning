# Loan EMI Calculator

A Python command-line application that calculates monthly loan installments (EMI), total repayment, and total interest payable based on the loan amount, annual interest rate, and loan duration.

## Features

- Accepts loan amount, annual interest rate, and loan duration.
- Calculates monthly EMI using the standard EMI formula.
- Calculates total repayment and total interest.
- Handles zero-interest loans.
- Validates invalid numeric inputs and rejects non-positive loan amounts and durations.

## How to Run

Make sure Python 3 is installed.

```bash
python3 problems/loan_emi_calculator/main.py
```

## Example Input

- Loan amount: ₹500,000
- Annual interest rate: 8.5%
- Loan duration: 5 years

## Concepts Used

- Variables and data types
- User input and type conversion
- Functions
- Conditional statements
- `while` loops
- `try` and `except`
- Arithmetic operators
- Rounding results with `round()`

## Limitations

This is an educational calculator. Actual lender EMIs may differ because of fees, insurance, rounding, and lender-specific terms.