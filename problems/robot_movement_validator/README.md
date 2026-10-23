# Robot Movement Validator

## 📌 Problem Statement

A robot moves across a coordinate grid to reach its destination. It can move in one of three modes: **Horizontal**, **Vertical**, or **Diagonal**.

Given the starting coordinates `(x1, y1)`, destination coordinates `(x2, y2)`, and selected movement mode, determine whether the movement is valid.

### Movement Rules

- **Horizontal:** The robot must remain in the same row (`y1 == y2`).
- **Vertical:** The robot must remain in the same column (`x1 == x2`).
- **Diagonal:** The absolute differences between the x-coordinates and y-coordinates must be equal.

Moving to the same position is always considered invalid.

## 🧾 Example

**Input**
```text
2 3
5 3
Horizontal
```

**Output**
```text
Valid
```

## ⚙️ How It Works

1. Accept the starting and destination coordinates.
2. Ask the user to select a movement mode.
3. Check whether both positions are identical.
4. Validate the movement according to the selected mode.
5. Display `Valid` or `Invalid`.

## 🧠 Concepts Practiced

- Python functions
- `if`, `elif`, and `else`
- Logical conditions
- Absolute values using `abs()`
- User input and type conversion

## ▶️ How to Run

Run the following command from the repository root:

```bash
python3 problems/robot_movement_validator/main.py
```

**Note:** This project uses descriptive input prompts for interactive use. For an online judge, remove those prompts and follow the exact input/output format specified by the problem.
