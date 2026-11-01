# Parking Lot Management System

A menu-driven Python application that simulates a parking lot management system. It allows users to park vehicles, assign parking slots, remove vehicles, calculate parking fees, and monitor parking availability.

## Features

- Display all available and occupied parking slots.
- Park vehicles using their registration numbers.
- Automatically assign the first available parking slot.
- Prevent duplicate vehicle registrations.
- Prevent parking when all slots are occupied.
- Store vehicle owner's name and expected parking duration.
- Remove vehicles when they exit the parking lot.
- Generate parking receipts.
- Calculate parking fees based on actual parking hours.
- Display all currently parked vehicles.
- Show parking statistics and total revenue.
- Handle invalid inputs using exception handling.

## Parking Rules

- Total parking capacity: 10 vehicles.
- Each vehicle is assigned the first available slot.
- Parking fee: Rs. 20 per hour.
- Actual parking duration is entered when removing a vehicle.
- Revenue is updated only after a successful vehicle exit.
- Parking information is stored temporarily in memory.

## How to Run

Make sure Python 3 is installed.

Run the following command from the repository's root directory:

```bash
python3 problems/parking_lot_management_system/main.py
```

## Menu Options

1. Display Parking Slots
2. Park a Vehicle
3. Remove a Vehicle
4. Display Parked Vehicles
5. Parking Summary
6. Exit

## Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Lists
- Functions
- For loops and while loops
- Conditional statements
- User input and type conversion
- Exception handling
- Dictionary methods
- Basic arithmetic operations

## Example Parking Fee

If a vehicle is parked for 3 hours:

Parking Fee = 3 × Rs. 20 = Rs. 60

## Storage

Vehicle and parking information is stored in Python dictionaries. All records are reset when the application exits.

## Future Improvements

- Permanent storage using file handling.
- Different parking rates for different vehicle types.
- Parking duration tracking using actual timestamps.
- Daily and monthly revenue reports.
- Multiple parking floors.

---

**Project Status:** Completed and tested.