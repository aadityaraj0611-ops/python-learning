
products = {
    101: {"name": "Laptop", "price": 50000, "stock": 10, "sold": 0},
    102: {"name": "Smartphone", "price": 25000, "stock": 15, "sold": 0},
    103: {"name": "Headphones", "price": 2000, "stock": 20, "sold": 0},
    104: {"name": "Keyboard", "price": 1500, "stock": 12, "sold": 0},
    105: {"name": "Mouse", "price": 800, "stock": 25, "sold": 0}
}

customers = {}
carts = {}
orders = {}
payments = {}

next_customer_id = 1001
next_order_id = 1
next_payment_id = 1


def display_products():
    print("\n--- Available Products ---")

    for product_id, details in products.items():
        print("\nProduct ID:", product_id)
        print("Name:", details["name"])
        print("Price: Rs.", details["price"])
        print("Available Stock:", details["stock"])


def add_product():
    print("\n--- Add New Product ---")

    try:
        product_id = int(input("Enter product ID: "))

        if product_id in products:
            print("Product ID already exists.")
            return

        name = input("Enter product name: ").strip()

        if name == "":
            print("Product name cannot be empty.")
            return

        price = float(input("Enter product price: "))
        stock = int(input("Enter initial stock: "))

        if price <= 0 or stock < 0:
            print("Price must be positive and stock cannot be negative.")
            return

        products[product_id] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": 0
        }

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter product ID: "))

        if product_id not in products:
            print("Product does not exist.")
            return

        new_price = float(input("Enter new price: "))
        new_stock = int(input("Enter new stock quantity: "))

        if new_price <= 0 or new_stock < 0:
            print("Invalid price or stock quantity.")
            return

        products[product_id]["price"] = new_price
        products[product_id]["stock"] = new_stock

        print("Product updated successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def search_product():
    print("\n--- Search Product ---")

    try:
        product_id = int(input("Enter product ID: "))

        if product_id in products:
            details = products[product_id]

            print("Product Name:", details["name"])
            print("Price: Rs.", details["price"])
            print("Stock:", details["stock"])
        else:
            print("Product does not exist.")

    except ValueError:
        print("Please enter a valid product ID.")


def register_customer():
    global next_customer_id

    print("\n--- Customer Registration ---")

    name = input("Enter customer name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name == "" or phone == "" or email == "":
        print("All customer details are required.")
        return

    customer_id = next_customer_id

    customers[customer_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    next_customer_id += 1

    print("Customer registered successfully!")
    print("Customer ID:", customer_id)


def display_customers():
    print("\n--- Registered Customers ---")

    if len(customers) == 0:
        print("No customers registered.")
        return

    for customer_id, details in customers.items():
        print("\nCustomer ID:", customer_id)
        print("Name:", details["name"])
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def add_to_cart():
    print("\n--- Add Product to Cart ---")

    try:
        customer_id = int(input("Enter customer ID: "))

        if customer_id not in customers:
            print("Customer does not exist.")
            return

        product_id = int(input("Enter product ID: "))

        if product_id not in products:
            print("Product does not exist.")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if quantity > products[product_id]["stock"]:
            print("Insufficient stock.")
            return

        if customer_id not in carts:
            carts[customer_id] = {}

        current_quantity = carts[customer_id].get(product_id, 0)

        if current_quantity + quantity > products[product_id]["stock"]:
            print("Requested quantity exceeds available stock.")
            return

        carts[customer_id][product_id] = current_quantity + quantity

        print("Product added to cart successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def view_cart():
    print("\n--- View Shopping Cart ---")

    try:
        customer_id = int(input("Enter customer ID: "))

        if customer_id not in customers:
            print("Customer does not exist.")
            return

        if customer_id not in carts or len(carts[customer_id]) == 0:
            print("Shopping cart is empty.")
            return

        total = 0

        for product_id, quantity in carts[customer_id].items():
            details = products[product_id]
            subtotal = details["price"] * quantity

            print("\nProduct:", details["name"])
            print("Quantity:", quantity)
            print("Price:", details["price"])
            print("Subtotal:", subtotal)

            total += subtotal

        print("\nCart Total: Rs.", total)

    except ValueError:
        print("Please enter a valid customer ID.")


def remove_from_cart():
    print("\n--- Remove Product from Cart ---")

    try:
        customer_id = int(input("Enter customer ID: "))

        if customer_id not in customers:
            print("Customer does not exist.")
            return

        if customer_id not in carts:
            print("Shopping cart is empty.")
            return

        product_id = int(input("Enter product ID: "))

        if product_id not in carts[customer_id]:
            print("Product is not present in this cart.")
            return

        del carts[customer_id][product_id]

        print("Product removed from cart successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


def place_order():
    global next_order_id

    print("\n--- Place Order ---")

    try:
        customer_id = int(input("Enter customer ID: "))

        if customer_id not in customers:
            print("Customer does not exist.")
            return

        if customer_id not in carts or len(carts[customer_id]) == 0:
            print("Shopping cart is empty.")
            return

        subtotal = 0

        for product_id, quantity in carts[customer_id].items():
            if quantity > products[product_id]["stock"]:
                print("Insufficient stock for:", products[product_id]["name"])
                return

            subtotal += products[product_id]["price"] * quantity

        if subtotal >= 10000:
            discount_rate = 10
        elif subtotal >= 5000:
            discount_rate = 5
        else:
            discount_rate = 0

        discount = subtotal * discount_rate / 100
        final_amount = subtotal - discount

        order_id = next_order_id

        order_items = {}

        for product_id, quantity in carts[customer_id].items():
            order_items[product_id] = quantity

        orders[order_id] = {
            "customer_id": customer_id,
            "items": order_items,
            "subtotal": subtotal,
            "discount": discount,
            "total": final_amount,
            "status": "Placed",
            "payment_status": "Pending"
        }

        for product_id, quantity in carts[customer_id].items():
            products[product_id]["stock"] -= quantity
            products[product_id]["sold"] += quantity

        carts[customer_id] = {}

        next_order_id += 1

        print("Order placed successfully!")
        print("Order ID:", order_id)
        print("Subtotal: Rs.", subtotal)
        print("Discount:", discount_rate, "%")
        print("Discount Amount: Rs.", discount)
        print("Final Amount: Rs.", final_amount)

    except ValueError:
        print("Please enter a valid customer ID.")


def display_orders():
    print("\n--- All Orders ---")

    if len(orders) == 0:
        print("No orders available.")
        return

    for order_id, details in orders.items():
        print("\nOrder ID:", order_id)
        print("Customer:", customers[details["customer_id"]]["name"])
        print("Subtotal: Rs.", details["subtotal"])
        print("Discount: Rs.", details["discount"])
        print("Total: Rs.", details["total"])
        print("Order Status:", details["status"])
        print("Payment Status:", details["payment_status"])


def cancel_order():
    print("\n--- Cancel Order ---")

    try:
        order_id = int(input("Enter order ID: "))

        if order_id not in orders:
            print("Order does not exist.")
            return

        if orders[order_id]["status"] == "Cancelled":
            print("Order is already cancelled.")
            return

        if orders[order_id]["status"] == "Delivered":
            print("Delivered orders cannot be cancelled.")
            return

        customer_id = orders[order_id]["customer_id"]

        for product_id, quantity in orders[order_id]["items"].items():
            products[product_id]["stock"] += quantity
            products[product_id]["sold"] -= quantity

        orders[order_id]["status"] = "Cancelled"
        orders[order_id]["payment_status"] = "Refunded" if orders[order_id]["payment_status"] == "Paid" else "Cancelled"

        print("Order cancelled successfully!")

    except ValueError:
        print("Please enter a valid order ID.")


def update_order_status():
    print("\n--- Update Order Status ---")

    try:
        order_id = int(input("Enter order ID: "))

        if order_id not in orders:
            print("Order does not exist.")
            return

        if orders[order_id]["status"] in ["Cancelled", "Delivered"]:
            print("Order status cannot be updated.")
            return

        print("1. Processing")
        print("2. Shipped")
        print("3. Delivered")

        choice = input("Choose new status: ").strip()

        if choice == "1":
            orders[order_id]["status"] = "Processing"
        elif choice == "2":
            orders[order_id]["status"] = "Shipped"
        elif choice == "3":
            orders[order_id]["status"] = "Delivered"
        else:
            print("Invalid status choice.")
            return

        print("Order status updated successfully!")

    except ValueError:
        print("Please enter a valid order ID.")


def process_payment():
    global next_payment_id

    print("\n--- Process Payment ---")

    try:
        order_id = int(input("Enter order ID: "))

        if order_id not in orders:
            print("Order does not exist.")
            return

        if orders[order_id]["status"] == "Cancelled":
            print("Cannot pay for a cancelled order.")
            return

        if orders[order_id]["payment_status"] == "Paid":
            print("Payment has already been completed.")
            return

        print("Amount to Pay: Rs.", orders[order_id]["total"])
        print("1. UPI")
        print("2. Card")
        print("3. Cash on Delivery")

        choice = input("Select payment method: ").strip()

        if choice == "1":
            method = "UPI"
        elif choice == "2":
            method = "Card"
        elif choice == "3":
            method = "Cash on Delivery"
        else:
            print("Invalid payment method.")
            return

        payments[next_payment_id] = {
            "order_id": order_id,
            "amount": orders[order_id]["total"],
            "method": method
        }

        orders[order_id]["payment_status"] = "Paid"

        print("Payment successful!")
        print("Payment ID:", next_payment_id)
        print("Payment Method:", method)

        next_payment_id += 1

    except ValueError:
        print("Please enter a valid order ID.")


def customer_order_history():
    print("\n--- Customer Order History ---")

    try:
        customer_id = int(input("Enter customer ID: "))

        if customer_id not in customers:
            print("Customer does not exist.")
            return

        found = False

        for order_id, details in orders.items():
            if details["customer_id"] == customer_id:
                found = True

                print("\nOrder ID:", order_id)
                print("Subtotal: Rs.", details["subtotal"])
                print("Discount: Rs.", details["discount"])
                print("Total: Rs.", details["total"])
                print("Status:", details["status"])
                print("Payment:", details["payment_status"])

        if not found:
            print("No order history found.")

    except ValueError:
        print("Please enter a valid customer ID.")


def sales_report():
    print("\n--- Sales Report ---")

    total_sales = 0
    completed_payments = 0

    for order in orders.values():
        if order["payment_status"] == "Paid":
            total_sales += order["total"]
            completed_payments += 1

    print("Total Paid Sales: Rs.", total_sales)
    print("Completed Payments:", completed_payments)

    highest_sold = -1
    best_product = "No sales yet"

    for product_id, details in products.items():
        if details["sold"] > highest_sold:
            highest_sold = details["sold"]
            best_product = details["name"]

    print("Best-Selling Product:", best_product)
    print("Units Sold:", max(highest_sold, 0))


def main():
    while True:
        print("\n========== E-COMMERCE ORDER MANAGEMENT SYSTEM ==========")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Search Product")
        print("5. Register Customer")
        print("6. Display Customers")
        print("7. Add Product to Cart")
        print("8. View Shopping Cart")
        print("9. Remove Product from Cart")
        print("10. Place Order")
        print("11. Display Orders")
        print("12. Cancel Order")
        print("13. Update Order Status")
        print("14. Process Payment")
        print("15. Customer Order History")
        print("16. Sales Report")
        print("17. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            register_customer()
        elif choice == "6":
            display_customers()
        elif choice == "7":
            add_to_cart()
        elif choice == "8":
            view_cart()
        elif choice == "9":
            remove_from_cart()
        elif choice == "10":
            place_order()
        elif choice == "11":
            display_orders()
        elif choice == "12":
            cancel_order()
        elif choice == "13":
            update_order_status()
        elif choice == "14":
            process_payment()
        elif choice == "15":
            customer_order_history()
        elif choice == "16":
            sales_report()
        elif choice == "17":
            print("Thank you for using the E-commerce Order Management System!")
            break
        else:
            print("Invalid choice. Please select between 1 and 17.")


main()
