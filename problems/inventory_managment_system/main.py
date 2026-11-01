
inventory = {}


def add_product():
    product_id = input("Enter product ID: ").strip()

    if product_id in inventory:
        print("Product ID already exists!")
        return

    product_name = input("Enter product name: ").strip()

    if product_name == "":
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter initial stock quantity: "))

        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity cannot be negative!")
            return

        inventory[product_id] = {
            "name": product_name,
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully!")

    except ValueError:
        print("Invalid input! Enter a valid price and quantity.")


def display_products():
    if len(inventory) == 0:
        print("Inventory is empty!")
        return

    print("\n---------- ALL PRODUCTS ----------")

    for product_id, details in inventory.items():
        print("Product ID:", product_id)
        print("Name:", details["name"])
        print("Price: Rs.", details["price"])
        print("Stock:", details["quantity"])
        print("----------------------------------")


def search_product():
    product_id = input("Enter product ID to search: ").strip()

    if product_id in inventory:
        details = inventory[product_id]

        print("\nProduct found!")
        print("Product ID:", product_id)
        print("Name:", details["name"])
        print("Price: Rs.", details["price"])
        print("Stock:", details["quantity"])
    else:
        print("Product not found!")


def update_price():
    product_id = input("Enter product ID: ").strip()

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        new_price = float(input("Enter new price: "))

        if new_price <= 0:
            print("Price must be greater than zero!")
            return

        inventory[product_id]["price"] = new_price
        print("Product price updated successfully!")

    except ValueError:
        print("Invalid price!")


def add_stock():
    product_id = input("Enter product ID: ").strip()

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        inventory[product_id]["quantity"] += quantity

        print("Stock added successfully!")
        print("Updated stock:", inventory[product_id]["quantity"])

    except ValueError:
        print("Invalid quantity!")


def sell_product():
    product_id = input("Enter product ID: ").strip()

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        available_stock = inventory[product_id]["quantity"]

        if quantity > available_stock:
            print("Insufficient stock!")
            print("Available stock:", available_stock)
            return

        inventory[product_id]["quantity"] -= quantity

        total_bill = quantity * inventory[product_id]["price"]

        print("\nSale successful!")
        print("Product:", inventory[product_id]["name"])
        print("Quantity sold:", quantity)
        print("Total bill: Rs.", round(total_bill, 2))
        print("Remaining stock:", inventory[product_id]["quantity"])

    except ValueError:
        print("Invalid quantity!")


def low_stock_products():
    found = False

    print("\n---------- LOW STOCK PRODUCTS ----------")

    for product_id, details in inventory.items():
        if details["quantity"] < 5:
            print("Product ID:", product_id)
            print("Name:", details["name"])
            print("Remaining stock:", details["quantity"])
            print("----------------------------------------")
            found = True

    if not found:
        print("No low-stock products found!")


def calculate_inventory_value():
    total_value = 0

    for details in inventory.values():
        total_value += details["price"] * details["quantity"]

    print("Total inventory value: Rs.", round(total_value, 2))


def main():
    while True:
        print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Update Product Price")
        print("5. Add Stock")
        print("6. Sell Product")
        print("7. Display Low-Stock Products")
        print("8. Calculate Total Inventory Value")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            display_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_price()

        elif choice == "5":
            add_stock()

        elif choice == "6":
            sell_product()

        elif choice == "7":
            low_stock_products()

        elif choice == "8":
            calculate_inventory_value()

        elif choice == "9":
            print("Thank you for using Inventory Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 9.")


main()
