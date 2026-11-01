# Inventory Management System

A Python-based command-line application that helps manage product inventory, track stock levels, update prices, and calculate the total value of available stock.

## Features

- Add new products with unique product IDs.
- Display all available products.
- Search for products using their IDs.
- Update product prices.
- Add new stock to existing products.
- Sell products and automatically reduce stock.
- Prevent sales when available stock is insufficient.
- Identify products with fewer than 5 units in stock.
- Calculate the total inventory value.
- Handle invalid inputs using exception handling.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python3 main.py
```

## Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Functions
- Conditional statements
- While loops and for loops
- Exception handling (`try-except`)
- String handling
- Arithmetic operations
- Built-in functions

## Data Storage

Product information is stored in a nested Python dictionary during program execution.

**Note:** This project uses temporary in-memory storage. Product information is not saved after the program exits.

## Testing

All 15 manual test cases passed successfully, including product creation, duplicate ID handling, stock updates, sales, insufficient stock, low-stock detection, and inventory valuation.

## Future Improvements

- Save inventory data permanently using file handling.
- Add product categories.
- Generate sales reports.
- Track sales history.

## Project Status

Completed successfully.
