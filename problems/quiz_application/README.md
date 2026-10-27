# Quiz Application

A beginner-friendly, terminal-based Python quiz that tests basic Python knowledge and calculates the user's final score.

## Features

- Presents five multiple-choice questions.
- Provides four options for each question.
- Checks answers automatically.
- Tracks the score.
- Displays the correct answer when a response is incorrect.
- Calculates the final percentage.
- Displays feedback based on the final score.
- Accepts lowercase and uppercase answers.

## Example

**Input**

```text
Enter your answer (A/B/C/D): B
```

**Output**

```text
Correct answer!

===== Quiz Results =====
Your score: 5 / 5
Percentage: 100.0 %
Excellent work!
```

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/quiz_application/main.py
```

Answer each question by entering A, B, C, or D.

## Concepts Practiced

- Lists and indexing
- Functions
- `for` loops
- `if`, `elif`, and `else`
- User input and string methods
- Counters and arithmetic
- Percentage calculations
- The `len()` and `range()` functions

## Learning Objective

This project demonstrates how lists, loops, functions, and conditional statements can be combined to create an interactive quiz application.

## Limitations

- The quiz contains five predefined questions.
- Scores are not saved after the program exits.
- Invalid answers are counted as incorrect.
- The questions and correct answers must be edited in the source code to change the quiz.