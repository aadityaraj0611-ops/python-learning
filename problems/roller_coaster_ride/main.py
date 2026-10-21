height = int(input())
age = int(input())
if height < 120:
    print("Not Allowed")
elif height <= 140:
    if age < 5:
        print("Not Allowed")
    else:
        print("Must ride with Adult")
        print(200)
else:
    if age < 5:
        print("Not Allowed")
    elif age <= 12:
        print("Must ride with Adult")
        print(200)
    else:
        print("Can ride alone")
        print(300)