# Countdown Timer

A beginner-friendly Python project that counts down from a user-provided number of seconds and displays a message when the countdown finishes.

## Features

- Accepts a countdown duration in seconds.
- Displays the remaining time.
- Waits one second between countdown steps.
- Rejects zero and negative countdown durations.
- Displays a completion message when the timer reaches zero.

## Example

**Input**
```text
Enter countdown time in seconds: 3
```

**Output**
```text
Time remaining: 3
Time remaining: 2
Time remaining: 1
Time's up!
```

## How to Run

From the root directory of the repository, execute:

```bash
python3 problems/countdown_timer/main.py
```

Enter a positive whole number of seconds when prompted.

## Concepts Practiced

- Importing Python modules
- Using `time.sleep()`
- Variables and integer input
- `while` loops
- `if` and `else`
- Comparison operators
- Countdown logic

## Learning Objective

This project demonstrates how loops and Python's `time` module can be used to create a simple real-time countdown.

## Limitations

- The program expects integer input.
- The countdown is a basic demonstration and is not designed for precision timing.
- The timer runs only in the terminal.