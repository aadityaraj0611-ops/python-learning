
rooms = {
    101: {"type": "Single", "price": 1000, "status": "Available"},
    102: {"type": "Single", "price": 1000, "status": "Available"},
    201: {"type": "Double", "price": 1800, "status": "Available"},
    202: {"type": "Double", "price": 1800, "status": "Available"},
    301: {"type": "Deluxe", "price": 3000, "status": "Available"},
    302: {"type": "Deluxe", "price": 3000, "status": "Available"}
}

guests = {}
bookings = {}
payments = {}

next_guest_id = 1001
next_booking_id = 1
next_payment_id = 1


def register_guest():
    global next_guest_id

    print("\n--- Guest Registration ---")

    name = input("Enter guest name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name == "" or phone == "" or email == "":
        print("All guest details are required.")
        return

    guest_id = next_guest_id

    guests[guest_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    next_guest_id += 1

    print("Guest registered successfully!")
    print("Guest ID:", guest_id)


def display_guests():
    print("\n--- Registered Guests ---")

    if len(guests) == 0:
        print("No guests registered.")
        return

    for guest_id, details in guests.items():
        print("\nGuest ID:", guest_id)
        print("Name:", details["name"])
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_guest():
    print("\n--- Search Guest ---")

    try:
        guest_id = int(input("Enter guest ID: "))

        if guest_id in guests:
            details = guests[guest_id]

            print("Name:", details["name"])
            print("Phone:", details["phone"])
            print("Email:", details["email"])
        else:
            print("Guest does not exist.")

    except ValueError:
        print("Please enter a valid guest ID.")


def display_rooms():
    print("\n--- Room Details ---")

    for room_number, details in rooms.items():
        print("\nRoom Number:", room_number)
        print("Room Type:", details["type"])
        print("Price per Day: Rs.", details["price"])
        print("Status:", details["status"])


def check_room_availability():
    print("\n--- Check Room Availability ---")

    for room_number, details in rooms.items():
        if details["status"] == "Available":
            print(
                "Room:", room_number,
                "| Type:", details["type"],
                "| Price:", details["price"]
            )


def book_room():
    global next_booking_id

    print("\n--- Room Booking ---")

    try:
        guest_id = int(input("Enter guest ID: "))

        if guest_id not in guests:
            print("Guest does not exist.")
            return

        room_number = int(input("Enter room number: "))

        if room_number not in rooms:
            print("Room does not exist.")
            return

        if rooms[room_number]["status"] != "Available":
            print("Room is already booked.")
            return

        days = int(input("Enter number of days: "))

        if days <= 0:
            print("Number of days must be positive.")
            return

        booking_id = next_booking_id

        bookings[booking_id] = {
            "guest_id": guest_id,
            "room_number": room_number,
            "days": days,
            "status": "Booked"
        }

        rooms[room_number]["status"] = "Booked"

        next_booking_id += 1

        print("Room booked successfully!")
        print("Booking ID:", booking_id)

    except ValueError:
        print("Please enter valid numeric values.")


def display_bookings():
    print("\n--- Booking Records ---")

    if len(bookings) == 0:
        print("No bookings found.")
        return

    for booking_id, details in bookings.items():
        guest_id = details["guest_id"]
        room_number = details["room_number"]

        print("\nBooking ID:", booking_id)
        print("Guest Name:", guests[guest_id]["name"])
        print("Room Number:", room_number)
        print("Room Type:", rooms[room_number]["type"])
        print("Number of Days:", details["days"])
        print("Status:", details["status"])


def cancel_booking():
    print("\n--- Cancel Booking ---")

    try:
        booking_id = int(input("Enter booking ID: "))

        if booking_id not in bookings:
            print("Booking does not exist.")
            return

        if bookings[booking_id]["status"] == "Cancelled":
            print("Booking is already cancelled.")
            return

        if bookings[booking_id]["status"] != "Booked":
            print("This booking cannot be cancelled.")
            return

        room_number = bookings[booking_id]["room_number"]

        bookings[booking_id]["status"] = "Cancelled"
        rooms[room_number]["status"] = "Available"

        print("Booking cancelled successfully.")

    except ValueError:
        print("Please enter a valid booking ID.")


def check_in():
    print("\n--- Guest Check-in ---")

    try:
        booking_id = int(input("Enter booking ID: "))

        if booking_id not in bookings:
            print("Booking does not exist.")
            return

        if bookings[booking_id]["status"] != "Booked":
            print("Guest cannot check in for this booking.")
            return

        bookings[booking_id]["status"] = "Checked In"

        print("Guest checked in successfully.")

    except ValueError:
        print("Please enter a valid booking ID.")


def check_out():
    print("\n--- Guest Check-out ---")

    try:
        booking_id = int(input("Enter booking ID: "))

        if booking_id not in bookings:
            print("Booking does not exist.")
            return

        if bookings[booking_id]["status"] != "Checked In":
            print("Guest must have checked in before checkout.")
            return

        bookings[booking_id]["status"] = "Checked Out"

        print("Guest checked out successfully.")

    except ValueError:
        print("Please enter a valid booking ID.")


def generate_bill():
    global next_payment_id

    print("\n--- Generate Bill ---")

    try:
        booking_id = int(input("Enter booking ID: "))

        if booking_id not in bookings:
            print("Booking does not exist.")
            return

        if bookings[booking_id]["status"] != "Checked Out":
            print("Bill can only be generated after checkout.")
            return

        for payment in payments.values():
            if payment["booking_id"] == booking_id:
                print("Bill has already been generated.")
                return

        room_number = bookings[booking_id]["room_number"]
        days = bookings[booking_id]["days"]

        price_per_day = rooms[room_number]["price"]
        total_amount = price_per_day * days

        payments[next_payment_id] = {
            "booking_id": booking_id,
            "amount": total_amount
        }

        print("Bill generated successfully!")
        print("Room Price per Day: Rs.", price_per_day)
        print("Number of Days:", days)
        print("Total Amount: Rs.", total_amount)
        print("Payment ID:", next_payment_id)

        next_payment_id += 1

    except ValueError:
        print("Please enter a valid booking ID.")


def booking_history():
    print("\n--- Guest Booking History ---")

    try:
        guest_id = int(input("Enter guest ID: "))

        if guest_id not in guests:
            print("Guest does not exist.")
            return

        found = False

        for booking_id, details in bookings.items():
            if details["guest_id"] == guest_id:
                found = True

                print("\nBooking ID:", booking_id)
                print("Room Number:", details["room_number"])
                print("Days:", details["days"])
                print("Status:", details["status"])

                for payment_id, payment in payments.items():
                    if payment["booking_id"] == booking_id:
                        print("Payment ID:", payment_id)
                        print("Bill Amount: Rs.", payment["amount"])

        if not found:
            print("No booking history found.")

    except ValueError:
        print("Please enter a valid guest ID.")


def calculate_revenue():
    print("\n--- Hotel Revenue Report ---")

    total_revenue = 0

    for payment in payments.values():
        total_revenue += payment["amount"]

    print("Total Revenue: Rs.", total_revenue)


def main():
    while True:
        print("\n========== HOTEL RESERVATION MANAGEMENT SYSTEM ==========")
        print("1. Register Guest")
        print("2. Display Guests")
        print("3. Search Guest")
        print("4. Display All Rooms")
        print("5. Check Room Availability")
        print("6. Book Room")
        print("7. Display Bookings")
        print("8. Cancel Booking")
        print("9. Guest Check-in")
        print("10. Guest Check-out")
        print("11. Generate Bill")
        print("12. View Guest Booking History")
        print("13. Calculate Hotel Revenue")
        print("14. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_guest()
        elif choice == "2":
            display_guests()
        elif choice == "3":
            search_guest()
        elif choice == "4":
            display_rooms()
        elif choice == "5":
            check_room_availability()
        elif choice == "6":
            book_room()
        elif choice == "7":
            display_bookings()
        elif choice == "8":
            cancel_booking()
        elif choice == "9":
            check_in()
        elif choice == "10":
            check_out()
        elif choice == "11":
            generate_bill()
        elif choice == "12":
            booking_history()
        elif choice == "13":
            calculate_revenue()
        elif choice == "14":
            print("Thank you for using the Hotel Reservation Management System!")
            break
        else:
            print("Invalid choice. Please select between 1 and 14.")


main()
