def print_sequence(n):
    if n == 0:
        return
    print(n, end=" ")
    print_sequence(n-1)
    print(n, end=" ")

N = int(input())
print_sequence(N)