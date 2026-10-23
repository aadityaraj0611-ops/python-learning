def check_movement(x1, y1, x2, y2, mode):
    # Movement to the same position is always invalid
    if x1 == x2 and y1 == y2:
        return "Invalid"

    #check horizontal movement(same row)
    if mode == "Horizontal":
        if y1 == y2:
            return "Valid"

    #Check vertical movement(same column)
    elif mode == "Vertical":
        if x1 == x2:
            return "Valid"

    #Check diagonal movement (equal coordinate differences)
    elif mode == "Diagonal":
        if abs(x2-x1) == abs(y1-y2):
            return "Valid"

    # If none of the conditions are satisfied
    return "Invalid"

#Take input from the user
x1, y1 = map(int,input("Enter starting coordinates(x1 y1): ").split())
x2, y2 = map(int,input("Enter destination coordinates(x2,y2): ").split())
mode = input("Enter movement mode (Horizontal/Vertical/Diagonal): ".strip())


# Validate the movement and display the result
result = check_movement(x1, y1, x2, y2, mode)
print("Movement Status: ", result)