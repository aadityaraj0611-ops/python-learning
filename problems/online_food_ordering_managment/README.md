# Online Food Ordering Management System

A menu-driven Python application that simulates an online food ordering platform. Customers can register, browse food items, place orders, track order status, and view their order history.

## Features

- **Food Menu:** Displays food items, prices, and availability.
- **Customer Registration:** Registers customers with unique customer IDs and prevents duplicate phone numbers.
- **Shopping Cart:** Allows customers to add multiple food items and quantities to one order.
- **Bill Generation:** Calculates subtotal, 5% tax, applicable discounts, and final payable amount.
- **Order Management:** Displays order history and individual order details.
- **Order Tracking:** Updates order status to Preparing, Out for Delivery, or Delivered.
- **Order Cancellation:** Allows cancellation of eligible orders.
- **Sales Report:** Displays customer statistics, order statistics, and total revenue.

## Technologies Used

- Python 3
- Dictionaries
- Lists
- Loops
- Conditional statements
- Functions
- Exception handling

## Project Structure

```text
online_food_ordering_management/
│
├── main.py
└── README.md
```

## Discount Policy

| Order Subtotal | Discount |
|---|---|
| Below ₹500 | No discount |
| ₹500–₹999.99 | 5% |
| ₹1,000 and above | 10% |

An additional 5% tax is applied to the subtotal.

**Final Amount = Subtotal + Tax - Discount**

## Order Statuses

- Placed
- Preparing
- Out for Delivery
- Delivered
- Cancelled

Delivered orders cannot be cancelled.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python3 main.py
```

## Sample Food Menu

| Item ID | Food Item | Price |
|---|---|---:|
| 101 | Veg Burger | ₹80 |
| 102 | Paneer Pizza | ₹220 |
| 103 | Veg Biryani | ₹150 |
| 104 | Masala Dosa | ₹100 |
| 105 | Cold Coffee | ₹90 |
| 106 | French Fries | ₹70 |

## Limitations

- Data is stored in memory and resets when the application exits.
- Payments are simulated; no real payment gateway is integrated.
- The food menu is predefined.
- The application does not use a database.

## Future Improvements

- Persistent storage using files or a database.
- Admin functionality to manage food items.
- Real payment gateway integration.
- Customer order invoices.
- Food delivery partner management.
- Search and filtering for menu items.

## Author

Aditya Raj