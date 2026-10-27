def run_quiz():
    questions = [
        "Which language are we learning?",
        "Which keyword is used to define a function in Python?",
        "What is the output of 5 // 2",
        "Which data type stores True or False?",
        "Which loop repeats while a condition is true?"
    ]

    options = [
        ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        ["A. function", "B. define", "C. def", "D. fun"],
        ["A. 2.5", "B. 3", "C. 2", "D. 1"],
        ["A. int", "B. str", "C. list", "D. bool"],
        ["A. for", "B. while", "C. if", "D. def"]
    ]

    answers = ["B", "C", "C", "D", "B"]
    score = 0

    print("===== Python Quiz Application =====")
    for i in range(len(questions)):
        print("\nQuestion", i+1, ":", questions[i])

        for option in options[i]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == answers[i]:
            print("Correct answer!")
            score = score + 1
        else:
            print("Incorrect answer!")
            print("Correct answer: ", answers[i])

    percentage = (score/len(questions))*100

    print("\n===== Quiz Results =====")
    print("Your score: ", score, "/", len(questions))
    print("Percentage: ", round(percentage, 2), "%")

    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 50:
        print("Good efforts! Keep participating.")
    else:
        print("Keep learning and try again!")

run_quiz()