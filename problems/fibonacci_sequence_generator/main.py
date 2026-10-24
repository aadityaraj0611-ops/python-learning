def fibonacci(n):
    first = 0
    second = 1

    for i in range(n):
        print(first, end=" ")

        next_number = first + second
        first = second
        second = next_number

n = int(input("How many Fibonacci numbers do you want? "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence: ")
    fibonacci(n)
    print()