def display_products(products):
    print("\n======== VENDING MACHINE ========")
    print("Available Products:")

    for product in products:
        print(product, "-", products[product]["name"],
              "| Price: Rs.", products[product]["price"],
              "| Stock:", products[product]["stock"])

def purchase_product(products):
    display_products(products)

    choice = input("\nEnter product code: ").strip().upper()

    if choice not in products:
        print("Invalid product code.")
        return

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if quantity > products[choice]["stock"]:
        print("Sorry, insufficient stock.")
        return
    total_price = products[choice]["price"] * quantity
    print("Total amount: Rs.", round(total_price, 2))
    payment = float(input("Enter payment amount (Rs.): "))

    if payment < total_price:
        print("Insufficient payment. Transaction cancelled. ")
        return
    change = payment - total_price

    products[choice]["stock"] = (
        products[choice]["stock"] - quantity
    )

    print("\nPurchase successfull!")
    print("Product:", products[choice]["name"])
    print("Quantity:", quantity)
    print("Total paid: Rs.", round(total_price, 2))
    print("Change returned: Rs.", round(change, 2))

def view_inventory(products):
    print("\n========= REMAINING INVENTORY ==========")

    for product in products:
        print(
            products[product]["name"],
            "- Remaining stock:",
            products[product]["stock"]
        )

products = {
    "A1": {"name": "Chips", "price": 20, "stock": 10},
    "A2": {"name": "Chocolate", "price": 30, "stock": 8},
    "A3": {"name": "Juice", "price": 40, "stock": 6},
    "A4": {"name": "Water", "price": 15, "stock": 12}
}

print("Welcome to the Vending Machine!")

while True:
    print("\n========== MAIN MENU ==========")
    print("1. View Products")
    print("2. Purchase Product")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()


    if choice == "1":
        display_products(products)
    elif choice == "2":
        try:
            purchase_product(products)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        view_inventory(products)
    elif choice == "4":
        print("Thank you for using the vending machine!")
        break
    else:
        print("Invalid choice. Please select 1-4.")