days = int(input())
book = int(input())
status = int(input())


def Rental_duration():
    if days <= 0:
        return None
    elif days <= 3:
        fee = days * 1
    elif days <= 7:
        fee = days * 0.75
    else:
        fee = days * 0.50

    return fee


def Book_type(fee):
    if book == 1:
        fee += 2
    elif book == 2:
        fee *= 0.90

    return fee


def membership_status(fee):
    if status == 1:
        fee *= 0.90

    return fee


fee = Rental_duration()

if fee is None:
    print("Invalid rental duration")
else:
    fee = Book_type(fee)
    fee = membership_status(fee)
    print(int(fee))