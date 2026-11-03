# Vehicle Rental Management System

A menu-driven Python project that simulates a vehicle rental business. It allows customers to register, rent vehicles, return them, view rental records, and track payments and revenue.

## Features

- **Vehicle Listing:** Displays available vehicles, their types, rental prices, and current status.
- **Customer Registration:** Registers customers with unique customer IDs and prevents duplicate phone numbers.
- **Vehicle Rental:** Allows registered customers to rent available vehicles for a specified number of days.
- **Vehicle Return:** Calculates the final rental amount based on actual usage.
- **Late Return Charges:** Applies an additional 20% daily charge for each day beyond the originally booked duration.
- **Rental History:** Displays active and completed rental records.
- **Payment History:** Displays payment IDs, rental IDs, customers, and payment amounts.
- **Revenue Report:** Shows total revenue, customer statistics, rental statistics, and vehicle usage.

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
vehicle_rental_management/
│
├── main.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Open the project directory in VS Code.
3. Open the terminal.
4. Run:

```bash
python3 main.py
```

## Rental Calculation

The basic rental amount is calculated as:

`Daily Rental Price × Actual Rental Days`

If the customer exceeds the booked rental duration, an additional late charge is applied:

`Extra Days × Daily Rental Price × 20%`

**Final Amount = Basic Rental Amount + Late Charges**

## Sample Vehicles

| Vehicle ID | Vehicle Name | Type | Daily Rent |
|---|---|---|---:|
| 101 | Maruti Swift | Car | ₹1,500 |
| 102 | Hyundai Creta | Car | ₹2,500 |
| 103 | Royal Enfield Classic 350 | Bike | ₹800 |
| 104 | Honda Activa | Scooter | ₹400 |
| 105 | Toyota Innova | Car | ₹3,000 |

## Limitations

- Data is stored in memory and resets when the program exits.
- Payments are simulated; no real payment gateway is connected.
- The system uses a predefined vehicle inventory.

## Future Improvements

- Persistent storage using files or a database.
- Ability to add and remove vehicles.
- Customer rental invoices.
- Real payment gateway integration.
- Search and filtering for vehicles and customers.

## Author

Aditya Raj