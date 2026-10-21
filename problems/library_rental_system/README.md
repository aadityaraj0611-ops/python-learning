# Library Rental System

A Python program that calculates book rental fees based on rental duration, book type, and membership status.

## Inputs
Enter three integers, each on a separate line:
1. Rental duration in days
2. Book type: 1 = New Release, 2 = Classic, 3 = Children's Book
3. Membership: 1 = Premium, 2 = Basic

## Rental Fee Rules
- 1–3 days: Rs 1 per day
- 4–7 days: Rs 0.75 per day
- 8 or more days: Rs 0.50 per day
- Zero or negative days: Invalid rental duration

## Book Adjustments
- New Release: Add Rs 2
- Classic: Apply a 10% discount
- Children's Book: No adjustment

## Membership Adjustments
- Premium: Apply an additional 10% discount
- Basic: No adjustment

Book adjustments are applied before membership discounts. The final amount is converted to an integer before printing.

## Example

Input:
4
1
1

Output:
4

## How to Run
Run this command from the project folder:

python3 main.py

## Concepts Practiced
- Input and output
- Integer type conversion
- if/elif/else conditions
- Arithmetic and percentage calculations
- Logical conditions
- Type casting
