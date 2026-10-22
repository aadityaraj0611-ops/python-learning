num = int(input("Enter a number: "))
original = num
def sum_of_digits(n):
    total = 0
    while n>0:
        digit = n%10
        total+=digit
        n//=10
    return total
def number_of_digits(n):
    count = 0
    while n>0:
        digit  = n%10
        count+=1
        n//=10
    return count
def reverse_number(n):
    rev = 0
    while n>0:
        digit = n%10
        rev = rev*10 + digit
        n//=10
    return rev
def is_pallindrome(n):
    return n == reverse_number(n)

print("Sum of digits of ", original, "is:", sum_of_digits(original))
print("Number of digits in ", original, "is:", number_of_digits(original))
print("Reverse of ", original, "is:", reverse_number(original))
print(original, "is a palindrome:", is_pallindrome(original))