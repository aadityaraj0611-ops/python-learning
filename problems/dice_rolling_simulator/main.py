import random

while True:
    print("\n===== Dice Rolling Simulator =====")
    print("1. Roll one die")
    print("2. Roll two dice")
    print("3. Exit")


    choice = (input("Enter your choice: "))


    if choice == "1":
        dice = random.randint(1, 6)
        print("You rolled: ", dice)

    elif choice == "2":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print("First die:", die1)
        print("Second die:", die2)
        print("Total:", die1 + die2)

    elif choice == "3":
        print("Thanks for playing!")
        break

    else:
        print("Invalid CHoice. Please select 1, 2, or 3.")