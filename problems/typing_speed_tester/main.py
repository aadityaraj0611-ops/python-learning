import time
print("===== Typing Speed Tester =====")
print("Type the following sentence as quickly and accurately:\n")
sentence = "Python is a powerful programming language"

print(sentence)
input("\nPress Enter when you are ready to start...")

print("\n Start typing!")
start_time = time.time()

typed_text = input("Your text: ")

end_time = time.time()

time_taken = end_time - start_time

if typed_text.strip() == "":
    print("\nYou did not type anything.")
else:
    original_words = sentence.split()
    typed_words = typed_text.split()

    words_typed = len(typed_words)
    minutes_taken = time_taken/60

    if minutes_taken > 0:
        wpm = words_typed / minutes_taken
    else:
        wpm = 0

    correct_characters = 0
    total_characters = len(sentence)

    for i in range(min(len(sentence), len(typed_text))):
        if sentence[i] == typed_text[i]:
            correct_characters = correct_characters + 1

    accuracy = (correct_characters / total_characters) * 100

    print("\n===== Your Results =====")
    print("Time taken:", round(time_taken, 2), "seconds")
    print("Typing speed:", round(wpm, 2), "WPM")
    print("Accuracy:", round(accuracy, 2), "%")