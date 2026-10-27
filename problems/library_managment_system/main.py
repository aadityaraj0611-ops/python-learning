def view_books(books, borrowed):
    print("\n===== Library Books =====")

    for i in range(len(books)):
        if borrowed[i]:
            status = "Borrowed"
        else:
            status = "Available"
        print(i+i, ".", books[i], "-", status)

def borrow_book(books, borrowed):
    view_books(books, borrowed)

    choice = int(input("Enter the books number to borrow: "))

    if choice < 1 or choice > len(books):
        print("Invalid book number.")
    elif borrowed[choice - 1]:
        print("Sorry, this book is already borrowed.")
    else:
        borrowed[choice - 1] = True 
        print("You borrowed: ", books[choice - 1])

def return_book(books, borrowed):
    view_books(books, borrowed)

    choice = int(input("Enter the book number to reuturn: "))

    if choice < 1 or choice > len(books):
        print("Invalid book number.")
    elif not borrowed[choice - 1]:
        print("This book has not been borrowed.")
    else:
        borrowed[choice - 1] = False
        print("You returned:", books[choice - 1])

books = [
    "Python Basics",
    "Introduction to C",
    "Data Structures",
    "Computer Networks",
    "Operating Systems",
]

borrowed = [False, False, False, False, False]

while True:
    print("\n===== Library Managment System =====")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books(books, borrowed)
    elif choice == "2":
        borrow_book(books, borrowed)
    elif choice == "3":
        return_book(books, borrowed)
    elif choice == "4":
        print("Thank you for using the library system!")
        break 
    else:
        print("Invalid Choice. Please select 1-4.")