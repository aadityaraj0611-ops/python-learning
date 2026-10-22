def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Too low"
    elif guess > secret_number:
        return "Too high"
    else:
        return "Correct!"


secret_number = 7
attempts = 0
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))
    attempts += 1

    result = check_guess(guess, secret_number)
    print(result)

print(f"You guessed the number in {attempts} attempts.")