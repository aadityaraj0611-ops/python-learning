password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

score = 0

if len(password) >= 0:
    score = score + 1
if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_digit:
    score = score + 1
if has_special:
    score = score + 1

print("\n===== Password Strength Checker =====")

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password strength: Strong")