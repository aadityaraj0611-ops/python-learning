def add_expense(expenses):
    amount = float(input("Enter expense amount: "))

    if amount > 0:
        expenses.append(amount)
        print("Expense added successfully")
    else:
        print("Please enter a valid amount.")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expense recorded yet.")
    else:
        print("\n===== All Expenses =====")
        for i in range(len(expenses)):
            print("Expense", i + 1, ": ₹", expenses[i])


def view_total(expenses):
    total = 0

    for amount in expenses:
        total+=amount 

    print("Total spending: ₹", round(total, 2))


def check_budget(expenses, budget):
    total = 0

    for amount in expenses:
        total = total + amount

    remaining = budget - total

    print("Budget: ₹", round(budget, 2))
    print("Total spending: ₹", round(total, 2))
    print("Remaining budget: ₹", round(remaining, 2))

    if remaining < 0:
        print("You have exceeded your budget!")

budget = float(input("Enter your total budget: "))
expenses = []

if budget <= 0:
    print("Please enter a budget greater than zero.")
else:
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Check Remaining Budget")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            check_budget(expenses, budget)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid Choice. Please Select 1-5.")