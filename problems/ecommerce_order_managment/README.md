# E-commerce Order Management System

## Overview

The E-commerce Order Management System is a menu-driven Python application that simulates the basic operations of an online shopping platform.

It allows users to manage products, register customers, maintain shopping carts, place orders, process payments, track order statuses, and generate sales reports.

This project demonstrates the practical implementation of Python programming concepts through a real-world business use case.

## Features

### 1. Product Management
- Display all available products.
- Add new products.
- Update product details.
- Search for products using their IDs.
- Track available stock.

### 2. Customer Management
- Register new customers.
- Generate unique customer IDs.
- Display registered customer details.

### 3. Shopping Cart Management
- Add products to shopping carts.
- View cart contents.
- Remove products from carts.
- Calculate cart totals.

### 4. Order Management
- Place customer orders.
- Generate unique order IDs.
- Display all orders.
- Cancel existing orders.
- Automatically restore product stock after cancellation.
- Update order statuses.

### 5. Payment Management
- Simulate payments using:
  - UPI
  - Card
  - Cash on Delivery
- Maintain payment records.
- Track payment statuses.

### 6. Sales and Reporting
- Calculate total paid sales.
- Track completed payments.
- Identify the best-selling product.
- Calculate units sold.

### 7. Validation and Error Handling
- Validate customer IDs.
- Check product availability.
- Prevent purchases exceeding available stock.
- Prevent repeated order cancellations.
- Handle invalid menu and payment selections.

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Variables, conditional statements, loops, functions, dictionaries, nested dictionaries, lists, and exception handling.
- **Interface:** Command-line interface (CLI)

## Project Structure

```text
ecommerce_order_management/
│
├── main.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Open the project directory in VS Code.
3. Open the integrated terminal.
4. Execute:

```bash
python3 main.py
```

