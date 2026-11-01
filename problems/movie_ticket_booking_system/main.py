def display_movies(movies):
    print("\n========== AVAILABLE MOVIES ==========")

    for movie_id, details in movies.items():
        print(movie_id, "-", details["name"],
              "| Ticket Price: Rs.", details["price"])

def display_seats(movies):
    display_movies(movies)

    movie_id = input("\nEnter movie ID: ")

    if movie_id not in movies:
        print("Invalid movie ID!")
        return

    print("\nAvailable seats for", movies[movie_id]["name"])

    for seats in range(1, 11):
        if seats in movies[movie_id]["booked_seats"]:
            print("[X]", end=" ")
        else:
            print("[", seats, "]", end=" ")
    print("\n[X] = Booked")

def book_ticket(movies, bookings):
    display_movies(movies)

    movie_id = input("\nEnter movie ID: ")

    if movie_id not in movies:
        print("Invalid movie ID!")
        return

    print("\nAvailable seats:")

    for seats in range(1, 11):
        if seats not in movies[movie_id]["booked_seats"]:
            print(seats, end=" ")
    print()

    try:
        seat = int(input("Enter seat number: "))

        if seat < 1 or seat > 10:
            print("Invalid seat number!")
            return

        if seat in movies[movie_id]["booked_seats"]:
            print("Sorry! This seat is already booked.")
            return

        customer = input("Enter customer name: ")

        movies[movie_id]["booked_seats"].append(seat)
        
        booking_id = len(bookings) +1 

        bookings[booking_id] = {
            "customer": customer,
            "movie_id": movie_id,
            "seat": seat,
            "price": movies[movie_id]["price"]
        }
        print("\nBooking successful!")
        print("Booking ID:", booking_id)
        print("Customer:", customer)
        print("Movie:", movies[movie_id]["name"])
        print("Seat:", seat)
        print("Ticket Price: RS.", movies[movie_id]["price"])
    except ValueError:
        print("Invalid input! Enter a valid seat number.")
def cancel_booking(movies, bookings):
    if len(bookings) == 0:
        print("No bookings available to cancel.")
        return
    try:
        booking_id = int(input("Enter booking ID to cancel: "))

        if booking_id not in bookings:
            print("Booking ID not found!")
            return

        movie_id = bookings[booking_id]["movie_id"]
        seat = bookings[booking_id]["seat"]

        movies[movie_id]["booked_seats"].remove(seat)

        customer = bookings[booking_id]["customer"]

        del bookings[booking_id]

    except ValueError:
        print("Please enter a valid booking ID.")

def display_bookings(movies, bookings):
    if len(bookings) == 0:
        print("No bookings available.")
        return

    print("\n========== ALL BOOKINGS ==========")

    for booking_id, details in bookings.items():
        movie_name = movies[details["movie_id"]]["name"]

        print("\nBooking ID:", booking_id)
        print("Customer:", details["customer"])
        print("Movie:", movie_name)
        print("Seat:", details["seat"])
        print("Price: Rs.", details["price"])

def calculate_revenue(bookings):
    total = 0

    for details in bookings.values():
        total += details["price"]

    print("Total tickets sold:", len(bookings))
    print("Total revenue: Rs.", total)

def main():
    movies = {
        "1": {
            "name": "Avengers",
            "price": 250,
            "booked_seats": []
        },
        "2": {
            "name": "Interstellar",
            "price": 200,
            "booked_seats": []
        },
        "3": {
            "name": "Inception",
            "price": 180,
            "booked_seats": []
        }
    }

    bookings = {}

    while True:
        print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
        print("1. Display Movies")
        print("2. Display Available Seats")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. Display All Bookings")
        print("6. Calculate Revenue")
        print("7. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                display_movies(movies)
            elif choice == 2:
                display_seats(movies)
            elif choice == 3:
                book_ticket(movies, bookings)
            elif choice == 4:
                cancel_booking(movies, bookings)
            elif choice == 5:
                display_bookings(movies, bookings)
            elif choice == 6:
                calculate_revenue(bookings)
            elif choice == 7:
                print("Thank you for using the booking system!")
                break
            else:
                print("Invalid choice! Select between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a number.")
main()