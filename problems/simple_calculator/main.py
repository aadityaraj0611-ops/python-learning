a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
op = input("Enter the operator of which you want to do the operation: ")
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a/b
if op == "+":
    result = addition(a,b)
    print(f"The addition of {a} and {b} is {result}")
elif op == "-":
    result = subtraction(a,b)
    print(f"The subtraction of {a} and {b} is {result}")
elif op == "*":
    result = multiplication(a,b)
    print(f"The multiplication of {a} and {b} is {result}")
elif op == "/":
    result = division(a,b)
    print(f"The division of {a} and {b} is {result}")
else:
    print("Invalid Choice")
