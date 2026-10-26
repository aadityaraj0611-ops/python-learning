# ATM Simulator

A beginner-friendly Python project that simulates basic ATM operations using conditional statements and a while loop.

## Features

- Check account balance
- Deposit money into the account
- Withdraw money from the account
- Prevent withdrawals exceeding the available balance
- Reject zero or negative deposit and withdrawal amounts
- Handle invalid menu choices
- Exit the program safely

## Starting Balance

The account starts with a balance of ₹1,000.

## Example

```text
===== ATM Simulator =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice: 2
Enter amount to deposit: 500
Deposit successful!
Updated balance: ₹ 1500
```

## How to Run

Open a terminal in the root directory of the repository and run:

```bash
python3 problems/atm_simulator/main.py
```

Follow the on-screen menu to perform ATM operations.

## Concepts Practiced

- Variables
- User input and output
- `while` loops
- `if`, `elif`, and `else`
- Nested conditions
- Arithmetic operations
- Comparison operators
- `break` to exit a loop

## Learning Objective

This project demonstrates how basic Python concepts can be combined to build a simple interactive banking simulation.

**Note:** This is an educational project. It does not connect to a real bank or store account information permanently.