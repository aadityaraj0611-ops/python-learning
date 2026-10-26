number = int(input("Enter a decimal number: "))

print("\n===== Number Base Converter =====")
print("Decimal:", number)
print("Binary:", bin(number)[2:] if number >= 0 else "-" + bin(number)[3:])
print("Octal:", oct(number)[2:] if number >= 0 else "-" + oct(number)[3:])
print("Hexadecimal:", hex(number)[2:] if number >= 0 else "-" + oct(number)[3:])