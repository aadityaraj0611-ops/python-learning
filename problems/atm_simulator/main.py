balance = 1000

while True:
    print("\n===== ATM Simulator =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is: ₹", balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated balance: ₹", balance)
        else:
            print("Please enter a valid amount.")
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Please enter a valid amount")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Withdrawal Successful!")
            print("Update balance: ₹", balance)
    elif choice == 4:
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid Choice. Please selecte 1-4.")