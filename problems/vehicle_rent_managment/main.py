
vehicles = {
    101: {"name": "Maruti Swift", "type": "Car", "rent_per_day": 1500, "available": True, "total_rentals": 0},
    102: {"name": "Hyundai Creta", "type": "Car", "rent_per_day": 2500, "available": True, "total_rentals": 0},
    103: {"name": "Royal Enfield Classic 350", "type": "Bike", "rent_per_day": 800, "available": True, "total_rentals": 0},
    104: {"name": "Honda Activa", "type": "Scooter", "rent_per_day": 400, "available": True, "total_rentals": 0},
    105: {"name": "Toyota Innova", "type": "Car", "rent_per_day": 3000, "available": True, "total_rentals": 0}
}

customers = {}
rentals = {}
payments = {}

next_customer_id = 1001
next_rental_id = 1
next_payment_id = 1

total_revenue = 0


def display_vehicles():
    print("\n========== VEHICLE LIST ==========")

    for vehicle_id, vehicle in vehicles.items():
        print("\nVehicle ID:", vehicle_id)
        print("Name:", vehicle["name"])
        print("Type:", vehicle["type"])
        print("Rent per day: Rs.", vehicle["rent_per_day"])

        if vehicle["available"]:
            print("Status: Available")
        else:
            print("Status: Rented")

    print("==================================")


def register_customer():
    global next_customer_id

    name = input("Enter customer name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name == "" or phone == "":
        print("Name and phone number cannot be empty.")
        return

    for customer in customers.values():
        if customer["phone"] == phone:
            print("Customer with this phone number already exists.")
            return

    customers[next_customer_id] = {
        "name": name,
        "phone": phone,
        "total_rentals": 0
    }

    print("Customer registered successfully!")
    print("Customer ID:", next_customer_id)

    next_customer_id += 1


def display_customers():
    if len(customers) == 0:
        print("No customers registered yet.")
        return

    print("\n========== CUSTOMER LIST ==========")

    for customer_id, customer in customers.items():
        print("\nCustomer ID:", customer_id)
        print("Name:", customer["name"])
        print("Phone:", customer["phone"])
        print("Total Rentals:", customer["total_rentals"])


def rent_vehicle():
    global next_rental_id

    try:
        customer_id = int(input("Enter customer ID: "))
        vehicle_id = int(input("Enter vehicle ID: "))
        days = int(input("Enter number of rental days: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if customer_id not in customers:
        print("Customer not found.")
        return

    if vehicle_id not in vehicles:
        print("Vehicle not found.")
        return

    if days <= 0:
        print("Rental days must be greater than zero.")
        return

    vehicle = vehicles[vehicle_id]

    if not vehicle["available"]:
        print("Sorry, this vehicle is already rented.")
        return

    estimated_cost = vehicle["rent_per_day"] * days

    rentals[next_rental_id] = {
        "customer_id": customer_id,
        "vehicle_id": vehicle_id,
        "days": days,
        "estimated_cost": estimated_cost,
        "status": "Active",
        "final_cost": 0,
        "payment_id": None
    }

    vehicle["available"] = False
    vehicle["total_rentals"] += 1
    customers[customer_id]["total_rentals"] += 1

    print("\nVehicle rented successfully!")
    print("Rental ID:", next_rental_id)
    print("Customer:", customers[customer_id]["name"])
    print("Vehicle:", vehicle["name"])
    print("Rental Days:", days)
    print("Estimated Cost: Rs.", estimated_cost)

    next_rental_id += 1


def return_vehicle():
    global next_payment_id, total_revenue

    try:
        rental_id = int(input("Enter rental ID: "))
        actual_days = int(input("Enter actual number of days used: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if rental_id not in rentals:
        print("Rental record not found.")
        return

    rental = rentals[rental_id]

    if rental["status"] == "Completed":
        print("This vehicle has already been returned.")
        return

    if actual_days <= 0:
        print("Actual rental days must be greater than zero.")
        return

    vehicle_id = rental["vehicle_id"]
    customer_id = rental["customer_id"]

    daily_rate = vehicles[vehicle_id]["rent_per_day"]
    amount = daily_rate * actual_days

    if actual_days > rental["days"]:
        extra_days = actual_days - rental["days"]
        late_charge = extra_days * daily_rate * 0.20
        amount += late_charge
    else:
        late_charge = 0

    rentals[rental_id]["status"] = "Completed"
    rentals[rental_id]["final_cost"] = amount

    vehicles[vehicle_id]["available"] = True

    payments[next_payment_id] = {
        "rental_id": rental_id,
        "customer_id": customer_id,
        "amount": amount,
        "late_charge": late_charge
    }

    rentals[rental_id]["payment_id"] = next_payment_id

    total_revenue += amount

    print("\nVehicle returned successfully!")
    print("Rental ID:", rental_id)
    print("Customer:", customers[customer_id]["name"])
    print("Vehicle:", vehicles[vehicle_id]["name"])
    print("Actual Days:", actual_days)
    print("Rental Amount: Rs.", daily_rate * actual_days)
    print("Late Charge: Rs.", late_charge)
    print("Total Amount: Rs.", amount)
    print("Payment ID:", next_payment_id)

    next_payment_id += 1


def display_rental_history():
    if len(rentals) == 0:
        print("No rental records available.")
        return

    print("\n========== RENTAL HISTORY ==========")

    for rental_id, rental in rentals.items():
        customer = customers[rental["customer_id"]]
        vehicle = vehicles[rental["vehicle_id"]]

        print("\nRental ID:", rental_id)
        print("Customer:", customer["name"])
        print("Vehicle:", vehicle["name"])
        print("Booked Days:", rental["days"])
        print("Estimated Cost: Rs.", rental["estimated_cost"])
        print("Status:", rental["status"])

        if rental["status"] == "Completed":
            print("Final Cost: Rs.", rental["final_cost"])


def display_payment_history():
    if len(payments) == 0:
        print("No payments recorded yet.")
        return

    print("\n========== PAYMENT HISTORY ==========")

    for payment_id, payment in payments.items():
        customer = customers[payment["customer_id"]]

        print("\nPayment ID:", payment_id)
        print("Rental ID:", payment["rental_id"])
        print("Customer:", customer["name"])
        print("Amount: Rs.", payment["amount"])
        print("Late Charge: Rs.", payment["late_charge"])


def revenue_report():
    completed_rentals = 0
    active_rentals = 0

    for rental in rentals.values():
        if rental["status"] == "Completed":
            completed_rentals += 1
        else:
            active_rentals += 1

    print("\n========== REVENUE REPORT ==========")
    print("Total Revenue: Rs.", total_revenue)
    print("Total Customers:", len(customers))
    print("Total Rentals:", len(rentals))
    print("Active Rentals:", active_rentals)
    print("Completed Rentals:", completed_rentals)
    print("Total Payments:", len(payments))

    print("\nVehicle Rental Statistics:")

    for vehicle_id, vehicle in vehicles.items():
        print(vehicle["name"], "-", vehicle["total_rentals"], "rentals")


def main():
    while True:
        print("\n========== VEHICLE RENTAL MANAGEMENT SYSTEM ==========")
        print("1. Display Vehicles")
        print("2. Register Customer")
        print("3. Display Customers")
        print("4. Rent Vehicle")
        print("5. Return Vehicle")
        print("6. Display Rental History")
        print("7. Display Payment History")
        print("8. Revenue Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_vehicles()

        elif choice == "2":
            register_customer()

        elif choice == "3":
            display_customers()

        elif choice == "4":
            rent_vehicle()

        elif choice == "5":
            return_vehicle()

        elif choice == "6":
            display_rental_history()

        elif choice == "7":
            display_payment_history()

        elif choice == "8":
            revenue_report()

        elif choice == "9":
            print("Thank you for using Vehicle Rental Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
