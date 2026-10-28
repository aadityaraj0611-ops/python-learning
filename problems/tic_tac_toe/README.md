# Tic-Tac-Toe

A beginner-friendly, two-player Tic-Tac-Toe game built in Python and played in the terminal.

## Features

- Two-player gameplay using X and O.
- Displays a 3×3 game board.
- Allows players to choose positions from 1 to 9.
- Rejects invalid positions.
- Prevents players from selecting occupied positions.
- Detects winning rows, columns, and diagonals.
- Detects a draw when the board is full without a winner.
- Alternates turns between players automatically.

## How to Play

The board positions are numbered as follows:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Players take turns entering a position number. Player X goes first, followed by Player O.

The first player to place three marks in a row, column, or diagonal wins.

## How to Run

From the root directory of the repository, run:

```bash
python3 problems/tic_tac_toe/main.py
```

## Concepts Practiced

- Lists and list indexing
- Functions and parameters
- `while` and `for` loops
- `if`, `elif`, and `else`
- Boolean return values
- Logical operators
- Game-state tracking
- Input validation with conditions

## Learning Objective

This project demonstrates how Python functions, lists, loops, and conditional statements can be combined to create a complete two-player game.

## Limitations

- The game runs only in the terminal.
- The game expects numeric input for positions.
- The game state is not saved after exiting.
- There is no computer opponent; both players are human.