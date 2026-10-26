side_1 = float(input("Enter first side: "))
side_2 = float(input("Enter second side: "))
side_3 = float(input("Enter third side: "))

if side_1 <= 0 or side_2 <= 0 or side_3<= 0:
    print("Invalid side lengths")
elif side_1+side_2 <= side_3 or side_1+side_3 <= side_2 or side_2+side_3 <= side_1:
    print("Invalid Triangle")
else:
    print("Valid Triangle")
    if side_1 == side_2 and side_2 == side_3:
        print("Triangle type: Equilateral")
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")