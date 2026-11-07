
# Network Packet Analyzer Simulator

## Project Overview

The Network Packet Analyzer Simulator is a Python-based project that simulates basic network packet analysis.

It generates simulated network packets containing source IP addresses, destination IP addresses, protocols, and packet sizes. Users can analyze the generated packets, filter them by protocol, identify unusually large packets, and view network traffic statistics.

**Note:** This project simulates network traffic. It does not capture or monitor real network packets.

## Features

- **Packet Generation:** Generate random simulated network packets.
- **Packet Display:** View packet IDs, source IP addresses, destination IP addresses, protocols, and sizes.
- **Protocol Filtering:** Filter packets based on TCP, UDP, HTTP, or DNS.
- **Large Packet Detection:** Identify packets exceeding a specified size.
- **Traffic Statistics:** Calculate total packets, total data size, average packet size, and protocol distribution.
- **Packet Management:** Add new simulated packets.
- **Input Validation:** Handle invalid menu choices and incorrect inputs.

## Technologies Used

- Python 3
- Random Module
- Dictionaries
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling

## Project Structure

```text
network_packet_analyzer_simulator/
│
├── main.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aadityaraj0611-ops/python-learning.git
```

### 2. Navigate to the project directory

```bash
cd python-learning/problems/network_packet_analyzer_simulator
```

### 3. Run the program

```bash
python3 main.py
```

## Available Operations

| Option | Operation |
|---|---|
| 1 | Display all packets |
| 2 | Filter packets by protocol |
| 3 | Find unusually large packets |
| 4 | View network traffic statistics |
| 5 | Add a simulated packet |
| 6 | Exit the program |

## Sample Packet Information

Each simulated packet contains:

- Packet ID
- Source IP address
- Destination IP address
- Network protocol
- Packet size in bytes

## Learning Outcomes

Through this project, I practiced:

- Working with lists and dictionaries.
- Generating random data using Python.
- Organizing code using functions.
- Filtering data using conditional statements.
- Performing calculations on collections.
- Handling invalid inputs using exception handling.
- Building an interactive menu-driven application.

## Future Improvements

- Save packet information to a text or CSV file.
- Generate graphical traffic statistics.
- Add packet search functionality.
- Introduce additional simulated network protocols.

---

**Author:** Aditya Raj
