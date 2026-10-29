def calculate_mileage(distance, fuel_used):
    return distance / fuel_used

def calculate_fuel_required(distance, mileage):
    return distance / mileage

def calculate_fuel_cost(fuel_required, fuel_price):
    return fuel_required * fuel_price

print("===== Fuel Cost and Mileage Calculator =====")

while True:
    print("\n===== Main Menu =====")
    print("1. Calculate vehicle mileage")
    print("2. Calculate journey fuel cost")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        distance = float(input("Enter distance traveled (km): "))
        fuel_used = float(input("Enter fuel consumed (liters): "))

        if distance <= 0 or fuel_used <= 0:
            print("Distance and fuel consumed must be greater than zero.")
        else:
            mileage = calculate_mileage(distance, fuel_used)
            print("vehicle mileage:", round(mileage, 2), "Km/L")
    elif choice == "2":
        distance = float(input("Enter journey distance (km): "))
        mileage = float(input("Enter vehicle mileaege (km/L): "))
        fuel_price = float(input("Enter fuel price per liter (₹): "))

        if distance <= 0 or mileage <= 0 or fuel_price <= 0:
            print("ALL values must be greater than zero.")
        else:
            fuel_required = calculate_fuel_required(distance, mileage)
            total_cost = calculate_fuel_cost(fuel_required, fuel_price)

            print("Fuel required:", round(fuel_required, 2), "liters")
            print("Estimated fuel cost: ₹", round(total_cost, 2))

    elif choice == "3":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid Choice. Please select 1, 2, or 3.")