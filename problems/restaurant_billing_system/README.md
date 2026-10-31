# Restaurant Billing System

A beginner-friendly Python project that simulates a restaurant billing application. Customers can select food items, specify quantities, and receive an automatically calculated bill.

## Features

- Displays a restaurant menu with item prices.
- Allows customers to order multiple food items.
- Accepts quantities for each item.
- Combines quantities when the same item is ordered again.
- Calculates the subtotal.
- Applies a 10% discount when the subtotal exceeds ₹1,000.
- Calculates 5% GST after the discount.
- Displays an itemized final bill.
- Handles invalid menu choices, quantities, and non-numeric input.

## Menu

| Item | Price |
|---|---:|
| Burger | ₹120 |
| Pizza | ₹250 |
| Sandwich | ₹100 |
| French Fries | ₹80 |
| Cold Coffee | ₹90 |

## How to Run

```bash
python3 problems/restaurant_billing_system/main.py
```

## Concepts Practiced

- Variables and data types
- Lists and dictionaries concepts
- Conditional statements
- Loops
- Functions
- List operations
- Arithmetic calculations
- Exception handling (`try` and `except`)
- User input and type conversion

## Discount and Tax Rules

- A 10% discount is applied when the subtotal is greater than ₹1,000.
- GST of 5% is calculated on the amount after the discount.

## Future Improvements

- Add more food items.
- Allow customers to remove items.
- Save bills to a file.
- Add customer details and order history.

---

**Project:** Restaurant Billing System  
**Language:** Python 3