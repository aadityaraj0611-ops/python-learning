# Number property analyzer
def is_Prime(n):
    if n <= 1:
        return False

    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count+=1

    return count == 2

def is_perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

def is_armstrong(n):
    if n < 0:
        return False

    original = n
    digits = 0
    temp = n

    if temp == 0:
        digits = 1
    else:
        while temp > 0:
            digits+=1
            temp//=10

    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == original

# Main Program 

number = int(input("Enter a positive integer: "))

print("\n--- Number Property Results ---")


if is_Prime(number):
    print(number, "is a Prime Number")
else:
    print(number,"is not a Prime Number")

if is_perfect(number):
    print(number, "is a Perfect Number")
else:
    print(number, "is not a Perfect Number")

if is_armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number")