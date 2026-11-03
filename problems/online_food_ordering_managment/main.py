
menu = {
    101: {"name": "Veg Burger", "price": 80, "available": True},
    102: {"name": "Paneer Pizza", "price": 220, "available": True},
    103: {"name": "Veg Biryani", "price": 150, "available": True},
    104: {"name": "Masala Dosa", "price": 100, "available": True},
    105: {"name": "Cold Coffee", "price": 90, "available": True},
    106: {"name": "French Fries", "price": 70, "available": True}
}

customers = {}
orders = {}
next_customer_id = 1001
next_order_id = 1

total_revenue = 0


def display_menu():
    print("\n========== RESTAURANT MENU ==========")

    for item_id, item in menu.items():
        print("\nItem ID:", item_id)
        print("Name:", item["name"])
        print("Price: Rs.", item["price"])

        if item["available"]:
            print("Status: Available")
        else:
            print("Status: Unavailable")

    print("=====================================")


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
        "total_orders": 0
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
        print("Total Orders:", customer["total_orders"])


def place_order():
    global next_order_id

    try:
        customer_id = int(input("Enter customer ID: "))
    except ValueError:
        print("Invalid customer ID.")
        return

    if customer_id not in customers:
        print("Customer not found.")
        return

    cart = {}
    cart_total = 0

    while True:
        display_menu()

        print("\nEnter 0 to finish adding items.")

        try:
            item_id = int(input("Enter food item ID: "))
        except ValueError:
            print("Please enter a valid item ID.")
            continue

        if item_id == 0:
            break

        if item_id not in menu:
            print("Food item not found.")
            continue

        if not menu[item_id]["available"]:
            print("This food item is currently unavailable.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if item_id in cart:
            cart[item_id]["quantity"] += quantity
        else:
            cart[item_id] = {
                "name": menu[item_id]["name"],
                "price": menu[item_id]["price"],
                "quantity": quantity
            }

        cart_total += menu[item_id]["price"] * quantity

        print("Item added to cart successfully!")

    if len(cart) == 0:
        print("Your cart is empty. Order not placed.")
        return

    tax = cart_total * 0.05

    discount = 0

    if cart_total >= 1000:
        discount = cart_total * 0.10
    elif cart_total >= 500:
        discount = cart_total * 0.05

    final_amount = cart_total + tax - discount

    orders[next_order_id] = {
        "customer_id": customer_id,
        "items": cart,
        "subtotal": cart_total,
        "tax": tax,
        "discount": discount,
        "final_amount": final_amount,
        "status": "Placed"
    }

    customers[customer_id]["total_orders"] += 1

    print("\n========== ORDER BILL ==========")
    print("Order ID:", next_order_id)
    print("Customer:", customers[customer_id]["name"])

    for item in cart.values():
        print(
            item["name"],
            "x", item["quantity"],
            "= Rs.", item["price"] * item["quantity"]
        )

    print("--------------------------------")
    print("Subtotal: Rs.", cart_total)
    print("Tax (5%): Rs.", round(tax, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Amount: Rs.", round(final_amount, 2))
    print("================================")

    next_order_id += 1


def display_orders():
    if len(orders) == 0:
        print("No orders available.")
        return

    print("\n========== ORDER HISTORY ==========")

    for order_id, order in orders.items():
        customer = customers[order["customer_id"]]

        print("\nOrder ID:", order_id)
        print("Customer:", customer["name"])

        print("Items:")

        for item in order["items"].values():
            print(
                item["name"],
                "x", item["quantity"]
            )

        print("Subtotal: Rs.", order["subtotal"])
        print("Tax: Rs.", round(order["tax"], 2))
        print("Discount: Rs.", round(order["discount"], 2))
        print("Final Amount: Rs.", round(order["final_amount"], 2))
        print("Status:", order["status"])


def update_order_status():
    try:
        order_id = int(input("Enter order ID: "))
    except ValueError:
        print("Please enter a valid order ID.")
        return

    if order_id not in orders:
        print("Order not found.")
        return

    if orders[order_id]["status"] == "Cancelled":
        print("This order has already been cancelled.")
        return

    if orders[order_id]["status"] == "Delivered":
        print("This order has already been delivered.")
        return

    print("\n1. Preparing")
    print("2. Out for Delivery")
    print("3. Delivered")

    choice = input("Select new status: ")

    if choice == "1":
        orders[order_id]["status"] = "Preparing"
    elif choice == "2":
        orders[order_id]["status"] = "Out for Delivery"
    elif choice == "3":
        orders[order_id]["status"] = "Delivered"
    else:
        print("Invalid status choice.")
        return

    print("Order status updated successfully!")


def cancel_order():
    global total_revenue

    try:
        order_id = int(input("Enter order ID: "))
    except ValueError:
        print("Please enter a valid order ID.")
        return

    if order_id not in orders:
        print("Order not found.")
        return

    order = orders[order_id]

    if order["status"] == "Cancelled":
        print("This order has already been cancelled.")
        return

    if order["status"] == "Delivered":
        print("Delivered orders cannot be cancelled.")
        return

    order["status"] = "Cancelled"

    customers[order["customer_id"]]["total_orders"] -= 1

    print("Order cancelled successfully!")


def sales_report():
    global total_revenue

    total_orders = len(orders)
    active_orders = 0
    cancelled_orders = 0
    delivered_orders = 0
    total_revenue = 0

    for order in orders.values():
        if order["status"] == "Cancelled":
            cancelled_orders += 1
        else:
            total_revenue += order["final_amount"]

            if order["status"] == "Delivered":
                delivered_orders += 1
            else:
                active_orders += 1

    print("\n========== SALES REPORT ==========")
    print("Total Customers:", len(customers))
    print("Total Orders:", total_orders)
    print("Active Orders:", active_orders)
    print("Delivered Orders:", delivered_orders)
    print("Cancelled Orders:", cancelled_orders)
    print("Total Revenue: Rs.", round(total_revenue, 2))
    print("==================================")


def main():
    while True:
        print("\n========== ONLINE FOOD ORDERING SYSTEM ==========")
        print("1. Display Food Menu")
        print("2. Register Customer")
        print("3. Display Customers")
        print("4. Place Order")
        print("5. Display Order History")
        print("6. Update Order Status")
        print("7. Cancel Order")
        print("8. Sales Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            register_customer()

        elif choice == "3":
            display_customers()

        elif choice == "4":
            place_order()

        elif choice == "5":
            display_orders()

        elif choice == "6":
            update_order_status()

        elif choice == "7":
            cancel_order()

        elif choice == "8":
            sales_report()

        elif choice == "9":
            print("Thank you for using Online Food Ordering System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
