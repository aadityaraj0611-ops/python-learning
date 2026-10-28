
# Typing Speed Tester

A beginner-friendly Python project that measures typing speed and accuracy.

## Features

- Displays a sentence for the user to type.
- Measures the time taken to type.
- Calculates typing speed in words per minute (WPM).
- Calculates typing accuracy as a percentage.
- Handles empty input.

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/typing_speed_tester/main.py
```

## Concepts Used

- Variables and data types
- User input and output
- Strings and string methods
- Lists and `split()`
- Loops and conditional statements
- The `time` module
- Basic mathematical calculations
- `round()` and `min()`

## How It Works

1. The program displays a sentence.
2. The user presses Enter when ready.
3. The timer starts when the typing prompt appears.
4. The program measures the elapsed time.
5. It calculates words per minute and character accuracy.
6. It displays the results.

## Limitations

- The test uses one fixed sentence.
- Accuracy compares characters at matching positions.
- The results are not saved after the program exits.
