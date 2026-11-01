
accounts = {}
transactions = []
next_account_number = 1001


def create_account():
    global next_account_number

    name = input("Enter customer name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    try:
        initial_balance = float(input("Enter initial deposit: "))

        if initial_balance < 0:
            print("Initial deposit cannot be negative!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    account_number = next_account_number
    next_account_number += 1

    accounts[account_number] = {
        "name": name,
        "balance": initial_balance
    }

    transactions.append({
        "account": account_number,
        "type": "Account Created",
        "amount": initial_balance
    })

    print("\nAccount created successfully!")
    print("Account Number:", account_number)


def display_accounts():
    if len(accounts) == 0:
        print("No accounts available!")
        return

    print("\n----- ALL BANK ACCOUNTS -----")

    for account_number, details in accounts.items():
        print("Account Number:", account_number)
        print("Customer Name:", details["name"])
        print("Balance: ₹", details["balance"])
        print("----------------------------")


def search_account():
    try:
        account_number = int(input("Enter account number: "))

        if account_number in accounts:
            print("\nAccount Found!")
            print("Account Number:", account_number)
            print("Customer Name:", accounts[account_number]["name"])
            print("Balance: ₹", accounts[account_number]["balance"])
        else:
            print("Account does not exist!")

    except ValueError:
        print("Enter a valid account number!")


def deposit_money():
    try:
        account_number = int(input("Enter account number: "))

        if account_number not in accounts:
            print("Account does not exist!")
            return

        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Deposit amount must be greater than zero!")
            return

        accounts[account_number]["balance"] += amount

        transactions.append({
            "account": account_number,
            "type": "Deposit",
            "amount": amount
        })

        print("Deposit successful!")
        print("Updated Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Please enter valid details!")


def withdraw_money():
    try:
        account_number = int(input("Enter account number: "))

        if account_number not in accounts:
            print("Account does not exist!")
            return

        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance!")
            return

        accounts[account_number]["balance"] -= amount

        transactions.append({
            "account": account_number,
            "type": "Withdrawal",
            "amount": amount
        })

        print("Withdrawal successful!")
        print("Remaining Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Please enter valid details!")


def transfer_money():
    try:
        sender = int(input("Enter sender account number: "))
        receiver = int(input("Enter receiver account number: "))

        if sender not in accounts or receiver not in accounts:
            print("One or both accounts do not exist!")
            return

        if sender == receiver:
            print("Cannot transfer money to the same account!")
            return

        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Transfer amount must be greater than zero!")
            return

        if amount > accounts[sender]["balance"]:
            print("Insufficient balance!")
            return

        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        transactions.append({
            "account": sender,
            "type": "Transfer Sent",
            "amount": amount
        })

        transactions.append({
            "account": receiver,
            "type": "Transfer Received",
            "amount": amount
        })

        print("Transfer completed successfully!")
        print("Sender Balance: ₹", accounts[sender]["balance"])
        print("Receiver Balance: ₹", accounts[receiver]["balance"])

    except ValueError:
        print("Please enter valid details!")


def transaction_history():
    try:
        account_number = int(input("Enter account number: "))

        if account_number not in accounts:
            print("Account does not exist!")
            return

        print("\n----- TRANSACTION HISTORY -----")
        print("Account Holder:", accounts[account_number]["name"])

        found = False

        for transaction in transactions:
            if transaction["account"] == account_number:
                found = True
                print(
                    transaction["type"],
                    "| Amount: ₹",
                    transaction["amount"]
                )

        if not found:
            print("No transactions found.")

        print("Current Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Enter a valid account number!")


def calculate_total_balance():
    total_balance = 0

    for details in accounts.values():
        total_balance += details["balance"]

    print("Total Money Held by Bank: ₹", total_balance)


def main():
    while True:
        print("\n========== BANKING SYSTEM ==========")
        print("1. Create New Account")
        print("2. Display All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. View Transaction History")
        print("8. Calculate Total Bank Balance")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            display_accounts()

        elif choice == "3":
            search_account()

        elif choice == "4":
            deposit_money()

        elif choice == "5":
            withdraw_money()

        elif choice == "6":
            transfer_money()

        elif choice == "7":
            transaction_history()

        elif choice == "8":
            calculate_total_balance()

        elif choice == "9":
            print("Thank you for using our Banking System!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
