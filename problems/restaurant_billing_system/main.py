def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("1. Burger          - Rs. 120")
    print("2. Pizza           - Rs. 250")
    print("3. Sandwich        - Rs. 100")
    print("4. French Fries    - Rs. 80")
    print("5. Cold Coffee     - Rs. 90")
    print("6. Checkout")
    print("=======================================")


def calculate_bill(items, quantities, prices):
    subtotal = 0

    print("\n=========== YOUR BILL =================")
    print("Item          Quantity       Amount")
    print("---------------------------------------")

    for i in range(len(items)):
        amount = prices[i] + quantities[i]
        subtotal = subtotal + amount

        print(items[i],"        ", quantities[i],"          Rs.", amount)
    print("-------------------------------------")
    print("Subtotal: Rs.", subtotal)

    discount = 0

    if subtotal > 1000:
        discount = subtotal * 0.10
        print("Discount (10%): Rs.", discount)
    else:
        print("Discount: Rs. 0")

    amount_after_discount = subtotal - discount

    gst = amount_after_discount * 0.05

    print("GST (5%): Rs.", gst)

    final_amount = amount_after_discount + gst

    print("-------------------------------------")
    print("FINAL AMOUNT: Rs.", round(final_amount, 2))
    print("======================================")

#Menu items and prices

menu_items = [
    "Burger",
    "Pizaa",
    "Sandwich",
    "French Fries",
    "Cold Coffee"
]

prices = [120, 250, 100, 80, 90]

# Customer order
ordered_items = []
ordered_quantities = []

print("WELCOME TO OUR RESTAURANT!")

while True:

    display_menu()

    try:
        choice = int(input("Enter your choice: "))

        if choice == 6:
            if len(ordered_items) == 0:
                print("You have not ordered anything yet.")
            else:
                calculate_bill(
                    ordered_items,
                    ordered_quantities,
                    prices
                )
                print("Thank you for visiting!")
                break
        elif choice >= 1 and choice <= 5:
            quantity = int(input("Enter quatity: "))

            if quantity <= 0:
                print("Please enter a valid positive quantity.")
            else:
                item_index = choice - 1
                item_name = menu_items[item_index]

                if item_name in ordered_items:
                    index = ordered_items.index(item_name)
                    ordered_quantities[index] += quantity

                else:
                    ordered_items.append(item_name)
                    ordered_quantities.append(quantity)
                print(quantity, item_name, "added to your order!")

        else:
            print("Invalid choice! Please select between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a number.")