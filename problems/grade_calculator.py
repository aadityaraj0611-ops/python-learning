marks = int(input("Enter your marks out of 100: "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks <= 89:
    print("B")
elif marks >= 70 and marks <=79:
    print("C")
elif marks >= 60 and marks <= 69:
    print("D")
else:
    print("F")