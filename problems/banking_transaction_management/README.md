# Banking Transaction Management System

## Project Overview

The Banking Transaction Management System is a menu-driven Python application that simulates basic banking operations. It allows users to create accounts, deposit and withdraw money, transfer funds between accounts, and view transaction histories.

The project demonstrates the use of Python fundamentals to build a practical command-line application.

## Features

1. **Create Bank Account** – Create a new account with a unique account number.
2. **Display All Accounts** – View all registered customer accounts and their balances.
3. **Search Account** – Find an account using its account number.
4. **Deposit Money** – Add money to an existing account.
5. **Withdraw Money** – Withdraw money while checking the available balance.
6. **Transfer Money** – Transfer funds between two different accounts.
7. **Transaction History** – View the recorded transactions of an account.
8. **Total Bank Balance** – Calculate the total money held across all accounts.
9. **Input Validation** – Handle invalid inputs, negative amounts, and insufficient balances.

## Technologies Used

- Python 3
- VS Code
- Terminal

## How to Run

1. Open the project folder in VS Code.
2. Open the Terminal.
3. Navigate to the project directory.
4. Run the following command:

```bash
python3 main.py
```

## Python Concepts Used

- Variables and data types
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions
- Dictionaries and nested dictionaries
- Lists
- Dictionary methods
- Exception handling (`try`, `except`)
- Arithmetic operations
- User input and output

## Data Storage

The application stores account details and transaction records in Python dictionaries and lists.

**Note:** All data is stored in memory. Account information and transaction history are lost when the application is closed.

## Testing

The application was tested for:

- Account creation and account searching
- Deposits and withdrawals
- Successful and unsuccessful transfers
- Insufficient balance handling
- Invalid account numbers
- Negative transaction amounts
- Transaction history
- Total bank balance calculation
- Invalid menu choices

All 16 test cases were completed successfully.

## Future Improvements

- Add PIN-based account authentication.
- Store account information permanently using file handling.
- Add account deletion functionality.
- Generate detailed bank statements.
- Add transaction dates and times.

## Project Status

Completed
