# Water Tank Monitoring Simulator

A Python command-line project that simulates filling and draining a water tank while monitoring its current water level.

## Features

- Set the tank's maximum capacity.
- View the current water level and available space.
- Fill the tank with a specified amount of water.
- Drain water from the tank.
- Prevent overflow and draining more water than is available.
- Reject zero or negative water amounts.
- Interactive menu that runs until the user exits.

## How to Run

Make sure Python 3 is installed.

```bash
python3 problems/water_tank_simulator/main.py
```

## Concepts Used

- Variables and data types
- User input and output
- Functions and parameters
- Conditional statements
- `while` loops
- Arithmetic operators
- Returning values from functions

## Limitations

- The water level resets to zero whenever the program restarts.
- Non-numeric input is not handled yet.
- This is a simulation and does not connect to real water tank sensors.