def display_slots(parking_slots):
    print("\n========== PARKING SLOT STATUS ==========")

    for slot, vehicle in parking_slots.items():
        if vehicle is None:
            print("Slot", slot, ": Available")
        else:
            print("Slot", slot, ": Occupied by", vehicle["number"])
def park_vehicle(parking_slots, parked_vehicles):
    vehicle_number = input("Enter vehicle registeration number: ").upper()
    print("DEBUG - Entered:", repr(vehicle_number))
    print("DEBUG - Registered:", list(parked_vehicles.keys()))

    if vehicle_number in parked_vehicles:
        print("This vehicle is already parked.")
        return
    available_slot = None

    for slot, vehicle in parking_slots.items():
        if vehicle is None:
            available_slot = slot
            break
    if available_slot is None:
        print("Parking lot is full!")
        return
    owner = input("Enter vehicle ownee's name: ")

    try:
        hours = int(input("Enter expected parking hours: "))
        if hours <= 0:
            print("Parking hours must be greater than zero.")
            return
        parking_slots[available_slot] = {
            "number": vehicle_number,
            "owner": owner,
            "hours": hours
        }
        parked_vehicles[vehicle_number] = {
            "slot": available_slot,
            "owner": owner,
            "hours": hours
        }
        print("\nVehicle parked successfully!")
        print("Assignment slot:", available_slot)
    except ValueError:
        print("Please enter a valid number of hours.")
def remove_vehicle(parking_slots, parked_vehicles, revenue):
    vehicle_number = input("Enter vehicle registeration number: ").upper()

    if vehicle_number not in parked_vehicles:
        print("Vehicle not found in the parking lot.")
        return revenue
    try:
        actual_hours = int(input("Enter actual parking hours: "))

        if actual_hours <= 0:
            print("Parking hours must be greater than zero.")
            return revenue

        slot = parked_vehicles[vehicle_number]["slot"]

        parking_fee = actual_hours * 20

        print("\n========== PARKING RECEIPT ==========")
        print("Vehicle:", vehicle_number)
        print("Owner:", parked_vehicles[vehicle_number]["owner"])
        print("Parking duration:", actual_hours, "hours")
        print("Rate: RS. 20 per hour")
        print("Total parking fee: RS.", parking_fee)
        parking_slots[slot] = None
        del parked_vehicles[vehicle_number]

        revenue += parking_fee

        print("Vehicle removed successfully!")
        return revenue
    except ValueError:
        print("Please enter a valid number of hours.")
        return revenue
def display_parked_vehicles(parked_vehicles):
    if len(parked_vehicles) == 0:
        print("No vehicles are currently parked.")
        return

    print("\n========== PARKED VEHICLES ==========")

    for vehicle_number, details in parked_vehicles.items():
        print("\nVehicle:", vehicle_number)
        print("Owner:", details["owner"])
        print("Slot:", details["slot"])
        print("Expected hours:", details["hours"])
def display_summary(parking_slots, parked_vehicles, revenue):
    occupied = len(parked_vehicles)
    available = len(parking_slots) - occupied

    print("\n========== PARKING SUMMARY ==========")
    print("Total parking slots:", len(parking_slots))
    print("Occupied slots:", occupied)
    print("Available slots:", available)
    print("Total vehicles currently parked:", occupied)
    print("Total revenue collected: Rs.", revenue)
def main():
    parking_slots = {}

    for slot in range(1, 11):
        parking_slots[slot] = None

    parked_vehicles = {}
    revenue = 0

    while True:
        print("\n===== PARKING LOT MANAGMENT SYSTEM =====")
        print("1. Display Parking Slots")
        print("2. Park a Vehicle")
        print("3. Remove a Vehicle")
        print("4. Display Parked Vehicles")
        print("5. Parking Summary")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                display_slots(parking_slots)
            elif choice == 2:
                park_vehicle(parking_slots, parked_vehicles)
            elif choice == 3:
                revenue = remove_vehicle(
                    parking_slots, parked_vehicles, revenue 
                )
            elif choice == 4:
                display_parked_vehicles(parked_vehicles)
            elif choice == 5:
                display_summary(parking_slots, parked_vehicles, revenue)
            elif choice == 6:
                print("Thank you for using the parking system!")
                break
            else:
                print("Invalid choice! Select between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")
main()