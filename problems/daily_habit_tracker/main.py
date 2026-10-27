def view_habits(habits, completed):
    print("\n===== Your Habits =====")

    if len(habits) == 0:
        print("No habits added yet.")
    else:
        for i in range(len(habits)):
            if completed[i]:
                status = "Completed"
            else:
                status = "Not completed"
            print(i + 1, ".", habits[i], "-", status)

def add_habit(habits, completed):
    habit = input("Enter a new habit: ").strip()

    if habit == "":
        print("Habit name cannot be empty.")
    else:
        habits.append(habit)
        completed.append(False)
        print("Habit added successfully!")

def mark_complete(habits, completed):
    view_habits(habits, completed)

    if len(habits) == 0:
        return 

    choice = int(input("Enter habit number to mark complete: "))
    if choice < 1 or choice > len(habits):
        print("Invalid habit number.")
    elif completed[choice - 1]:
        print("This habit is already completed.")
    else:
        completed[choice - 1] = True
        print("Habit marked as completed!")

def view_progress(habits, completed):
    total = len(habits)
    done = 0

    for status in completed:
        if status:
            done = done + 1

    print("\n===== Daily Progress =====")
    print("Total habits:", total)
    print("Completed habits:", done)

    if total > 0:
        percentage = (done/total)*100
        print("Completion percentage:", round(percentage, 2), "%")
    else:
        print("Add some habits to start tracking progress.")

habits = ["Study Python", "Exercise", "Read"]
completed = [False, False, False]

while True:
    print("\n===== Daily Habit Trackr ======")
    print("1. View Habits")
    print("2. Add Habit")
    print("3. Mark Habit Complete")
    print("4. View Progress")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_habits(habits, completed)
    elif choice == "2":
        add_habit(habits, completed)
    elif choice == "3":
        mark_complete(habits, completed)
    elif choice == "4":
        view_progress(habits, completed)
    elif choice == "5":
        print("THank you for using Daily Habit Tracker")
        break
    else:
        print("Invalid choice. Please select 1-5.")