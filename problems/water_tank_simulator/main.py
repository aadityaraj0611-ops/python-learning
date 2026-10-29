def display_status(Water_level, tank_capacity):
    print("\n===== Tank Status =====")
    print("Tank capacity:", tank_capacity, "liters")
    print("Current water level:", Water_level, "litres")
    print("Available space:", tank_capacity - Water_level, "litres")

def fill_tank(Water_level, tank_capacity):
    amount = float(input("Enter amount of water to add (litres): "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif Water_level + amount > tank_capacity:
        print("Cannot fill: the tank would overflow.")
        print("Available space:", tank_capacity - Water_level, "litres")
    else:
        Water_level = Water_level + amount
        print("Water added successfully!")
    return Water_level

def drain_tank(Water_level):
    amount = float(input("Enter amount of water to drain (liters): "))

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > Water_level:
        print("Cannot drain: insufficient water.")
    else:
        Water_level = Water_level - amount
        print("Water drained successfully!")

    return Water_level

print("===== Water Tank Monitoring Simulator =====")

tank_capacity = float(input("Enter tank capcity in liters: "))

while tank_capacity <= 0:
    print("Tank capcity must be greater than zero.")
    tank_capacity = float(input("Enter tank capacity in liters: "))

Water_level = 0

while True:
    print("\n===== Main Menu =====")
    print("1. View tank status")
    print("2. Fill tank")
    print("3. Drain tank")
    print("4. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        display_status(Water_level, tank_capacity)
    elif choice == "2":
        Water_level = fill_tank(Water_level, tank_capacity)
    elif choice == "3":
        Water_level = drain_tank(Water_level)
    elif choice == "4":
        print("Water Tank Simulator closed.")
        break

    else:
        print("Invalid choice. Please select 1-4.")