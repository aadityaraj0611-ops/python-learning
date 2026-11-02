# Hospital Management System

A menu-driven Hospital Management System built using Python. The project simulates basic hospital operations, including patient registration, doctor management, appointment booking, appointment cancellation, billing, and revenue calculation.

## Features

- **Patient Management**
  - Register new patients.
  - Display all registered patients.
  - Search patients using their patient ID.
  - Validate patient details and age.

- **Doctor Management**
  - Register doctors with their specialization and consultation fees.
  - Display all registered doctors.
  - Validate doctor details and consultation fees.

- **Appointment Management**
  - Book appointments for registered patients.
  - Prevent duplicate active appointments.
  - Display appointment details.
  - Cancel existing appointments.

- **Billing Management**
  - Generate patient bills.
  - Calculate total bills using consultation fees and treatment charges.
  - Display individual billing records.

- **Patient History**
  - View a patient's appointment and billing history.

- **Revenue Calculation**
  - Calculate total revenue from generated bills.

## Technologies Used

- Python 3
- Dictionaries
- Lists
- Loops
- Conditional statements
- Functions
- Exception handling

## How to Run

1. Open the project directory.
2. Open the terminal.
3. Run the following command:

```bash
python3 main.py
```

## Billing Formula

Total Bill = Consultation Fee + Treatment Charges

For example:

- Consultation Fee = ₹500
- Treatment Charges = ₹2,000
- **Total Bill = ₹2,500**

## Testing

The project was tested using 23 test cases covering:

- Patient registration and validation
- Patient searching
- Doctor registration and validation
- Appointment booking
- Duplicate appointment prevention
- Appointment cancellation
- Bill generation
- Invalid billing inputs
- Patient history
- Revenue calculation
- Program exit

All 23 test cases passed.

## Current Limitations

- Data is stored in memory and is lost when the program exits.
- Appointment dates and times are accepted as text and are not fully calendar-validated.
- This is an educational simulation, not a real hospital management or payment system.
- Billing is independent of appointment status.
- No authentication or patient-data security system is implemented.

## Future Improvements

- Add permanent data storage using files or a database.
- Add appointment date and time validation.
- Connect billing with appointment records.
- Add patient and doctor login systems.
- Add more detailed reports and billing features.

## Project Status

**Completed — all 23 test cases passed.**