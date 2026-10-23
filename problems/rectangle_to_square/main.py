def canFormSquare(l1, b1, l2, b2, l3, b3):
    if l1 == l2 == l3 and b1 + b2 + b3 == l1:
        return "YES"
    if b1 == b2 == b3 and l1 + l2 + l3 == b1:
        return "NO"
    if b2 + b3 == b1 and l2 == l3 and l1 + l2 == b1:
        return "YES"

    return "NOd"