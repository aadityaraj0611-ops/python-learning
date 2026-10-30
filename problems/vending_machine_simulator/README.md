# Vending Machine Simulator

A beginner-friendly Python project that simulates a vending machine. Users can view products, purchase items, make payments, and check the remaining inventory.

## Features

- Display available products and prices
- Purchase products using product codes
- Select the required quantity
- Validate stock availability
- Calculate total payment and change
- Update inventory after successful purchases
- Handle invalid inputs and insufficient payments

## Available Products

| Code | Product | Price | Stock |
|---|---|---:|---:|
| A1 | Chips | Rs. 20 | 10 |
| A2 | Chocolate | Rs. 30 | 8 |
| A3 | Juice | Rs. 40 | 6 |
| A4 | Water | Rs. 15 | 12 |

## How to Run

Open the repository's root directory in the terminal and execute:

```bash
python3 problems/vending_machine_simulator/main.py
```

## Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Functions
- `while` loops
- `for` loops
- Conditional statements (`if`, `elif`, `else`)
- User input using `input()`
- Exception handling using `try` and `except`
- Arithmetic operations
- String methods

## Limitations

- Inventory resets when the program is restarted.
- Product information is predefined.
- This is a terminal-based application.
- No database or permanent storage is used.

## Future Improvements

- Add an administrator menu to restock products.
- Store inventory permanently using files.
- Add more products and payment options.