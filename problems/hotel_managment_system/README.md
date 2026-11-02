# Hotel Reservation Management System

A menu-driven Hotel Reservation Management System built using Python. This project simulates hotel operations such as guest registration, room management, reservations, check-in, check-out, billing, and revenue calculation.

## Features

### 1. Guest Management
- Register new guests.
- Display all registered guests.
- Search guests using their unique guest ID.
- Validate guest information.

### 2. Room Management
- Display all available hotel rooms.
- View room types and prices.
- Check room availability.
- Automatically update room status after booking and cancellation.

### 3. Reservation Management
- Book rooms for registered guests.
- Prevent booking of already occupied rooms.
- Validate guest IDs, room numbers, and booking duration.
- Display all reservation records.
- Cancel existing reservations.

### 4. Check-in and Check-out
- Check in guests with valid bookings.
- Prevent repeated check-ins.
- Allow checkout only after check-in.
- Update booking status accordingly.

### 5. Billing System
- Generate bills after successful checkout.
- Calculate the total room charges.
- Prevent duplicate bill generation.
- Maintain payment records.

### 6. Booking History
- View a guest's previous bookings.
- Display booking status and payment details.

### 7. Revenue Management
- Calculate total hotel revenue from generated bills.

## Room Categories and Pricing

| Room Type | Room Numbers | Price per Day |
|---|---|---:|
| Single | 101, 102 | ₹1,000 |
| Double | 201, 202 | ₹1,800 |
| Deluxe | 301, 302 | ₹3,000 |

## Technologies Used

- Python 3
- Dictionaries and nested dictionaries
- Lists
- Loops
- Conditional statements
- Functions
- Exception handling

## Billing Formula

**Total Bill = Room Price per Day × Number of Days**

Example:

- Room Type: Double
- Price per Day: ₹1,800
- Number of Days: 2
- Total Bill: ₹3,600

## How to Run

Open the project directory in your terminal and execute:

```bash
python3 main.py
```

## Testing

The application was tested using 32 test cases covering:

- Guest registration and validation
- Guest searching
- Room display and availability
- Room reservations
- Duplicate booking prevention
- Booking cancellation
- Check-in and check-out
- Billing and duplicate bill prevention
- Guest booking history
- Revenue calculation
- Invalid inputs and nonexistent records

**All 32 test cases passed.**

## Current Limitations

- Data is stored in memory and resets when the program exits.
- Booking dates and actual stay durations are not tracked.
- Room availability is managed through booking status rather than calendar dates.
- Payments are simulated; no actual payment gateway is connected.
- Guest authentication and data security are not implemented.

## Future Improvements

- Add permanent data storage using files or a database.
- Implement date-based reservations.
- Support multiple bookings for the same room on different dates.
- Add payment status and payment methods.
- Introduce guest and administrator login systems.
- Generate detailed occupancy and revenue reports.

## Project Status

**Completed — all 32 test cases passed.**