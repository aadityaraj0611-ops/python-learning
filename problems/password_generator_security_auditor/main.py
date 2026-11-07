
import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_groups = []

    if use_upper:
        character_groups.append(string.ascii_uppercase)

    if use_lower:
        character_groups.append(string.ascii_lowercase)

    if use_digits:
        character_groups.append(string.digits)

    if use_symbols:
        character_groups.append("!@#$%^&*()-_=+[]{}?")

    if not character_groups:
        return None

    if length < len(character_groups):
        return None

    password = []

    # Include at least one character from every selected group.
    for group in character_groups:
        password.append(secrets.choice(group))

    all_characters = "".join(character_groups)

    # Fill the remaining length.
    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Securely shuffle the characters.
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def audit_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Consider using at least 12 characters.")

    if len(password) >= 16:
        score += 1
    else:
        suggestions.append("Consider using 16 or more characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    common_passwords = [
        "password",
        "password123",
        "123456",
        "123456789",
        "qwerty",
        "admin",
        "letmein",
        "welcome"
    ]

    if password.lower() in common_passwords:
        suggestions.append("This is a commonly used password. Choose a different one.")
        score = 0

    if len(password) > 0 and len(set(password)) == 1:
        suggestions.append("Avoid passwords containing only repeated characters.")
        score = 0

    if password.lower() in ["abcdef", "abcdefgh", "abcdefghij"]:
        suggestions.append("Avoid predictable sequences.")
        score = 0

    return score, suggestions


def show_password_strength(score):
    if score <= 2:
        print("Strength: Weak")
    elif score <= 4:
        print("Strength: Moderate")
    elif score <= 6:
        print("Strength: Strong")
    else:
        print("Strength: Very Strong")


def generate_single_password():
    print("\n--- Generate Password ---")

    try:
        length = int(input("Enter password length (8-128): "))

        if length < 8 or length > 128:
            print("Please enter a length between 8 and 128.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(
            length, use_upper, use_lower, use_digits, use_symbols
        )

        if password is None:
            print("Select at least one character category.")
            return

        print("\nGenerated Password:", password)
        print("Keep it private and store it in a trusted password manager.")

    except ValueError:
        print("Please enter a valid number.")


def generate_multiple_passwords():
    print("\n--- Generate Multiple Passwords ---")

    try:
        count = int(input("How many passwords do you want? (1-10): "))
        length = int(input("Enter password length (8-128): "))

        if count < 1 or count > 10:
            print("Please choose between 1 and 10 passwords.")
            return

        if length < 8 or length > 128:
            print("Password length must be between 8 and 128.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include special characters? (y/n): ").lower() == "y"

        print("\nGenerated Passwords:")

        for number in range(count):
            password = generate_password(
                length, use_upper, use_lower, use_digits, use_symbols
            )

            if password is None:
                print("Select at least one character category.")
                return

            print(number + 1, ".", password)

        print("\nStore your chosen password securely.")

    except ValueError:
        print("Please enter valid numbers.")


def check_password():
    print("\n--- Password Security Auditor ---")

    password = input("Enter a password to check: ")

    if password == "":
        print("Password cannot be empty.")
        return

    score, suggestions = audit_password(password)

    print("\nPassword Audit Results")
    print("----------------------")

    show_password_strength(score)

    print("Security score:", score, "/ 7")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password meets all the basic checks!")

    print("\nNote: This is a basic local check, not a guarantee of security.")


def show_security_tips():
    print("\n--- Password Security Tips ---")
    print("1. Use at least 12-16 characters.")
    print("2. Use a different password for every account.")
    print("3. Avoid names, birthdays, and predictable patterns.")
    print("4. Never share your passwords with anyone.")
    print("5. Use a trusted password manager.")
    print("6. Enable two-factor authentication wherever possible.")
    print("7. Never store passwords in plain-text files.")


def main():
    while True:
        print("\n===================================")
        print("     PASSWORD GENERATOR & AUDITOR")
        print("===================================")
        print("1. Generate a password")
        print("2. Generate multiple passwords")
        print("3. Check password strength")
        print("4. View password security tips")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            generate_single_password()

        elif choice == "2":
            generate_multiple_passwords()

        elif choice == "3":
            check_password()

        elif choice == "4":
            show_security_tips()

        elif choice == "5":
            print("Thank you for using Password Generator & Auditor!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


main()
