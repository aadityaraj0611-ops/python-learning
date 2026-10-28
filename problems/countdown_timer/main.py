import time

print("===== Countdown Timer =====")

seconds = int(input("Enter countdown time in seconds: "))

if seconds <= 0:
    print("Please enter a positive number of seconds.")
else:
    while seconds > 0:
        print("Time remaining:", seconds)
        time.sleep(1)
        seconds = seconds - 1

    print("Time's up!")