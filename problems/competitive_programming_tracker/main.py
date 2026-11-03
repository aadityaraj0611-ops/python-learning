problems = []

next_id = 1

def add_problem():
    global next_id

    print("\n---- Add Solved Problem ----")

    problem_name = input("Enter problem name: ")
    platform = input("Enter platform: ")
    problem_code = input("Enter problem ID/Code: ")
    difficulty = int(input("Enter difficulty rating: "))
    topic = input("Enter topic: ")


    problem = {
        "id": next_id,
        "problem_name": problem_name,
        "platform": platform,
        "problem_code": problem_code,
        "difficulty": difficulty,
        "topic": topic,
        "status": "Solved"
    }

    problems.append(problem)

    print("\nProblem added successfully!")
    print("Your Problem ID:", next_id)
    next_id += 1
def display_problems():
    print("\n--- Solved Problems ---")

    if len(problems) == 0:
        print("No Problems recorded yet.")
    else:
        for problem in problems:
            print("\nProblem ID:", problem["id"])
            print("Name:", problem["problem_name"])
            print("Platform:", problem["platform"])
            print("Problem Code:", problem["problem_code"])
            print("Difficulty:", problem["difficulty"])
            print("Topic:", problem["topic"])
            print("Status:", problem["status"])
def search_problems():
    print("\n--- Search Problem ---")

    search_value = input("Enter problem name, code, or platform: ").lower()

    found = False

    for problem in problems:
        if(search_value in problem["problem_name"].lower()
           or search_value in problem["problem_code"].lower()
           or search_value in problem["platform"].lower()):

            print("\nProblem Found!")
            print("Problem ID:", problem["id"])
            print("Name:", problem["problem_name"])
            print("Platform:", problem["platform"])
            print("Problem Code:", problem["problem_code"])
            print("Difficulty:", problem["difficulty"])
            print("Topic:", problem["topic"])
            print("Status:", problem["status"])

            found = True
        if found == False:
            print("No matching problem found.")

def main():
    while True:
        print("\n===== COMPETITIVE PROGRAMMING TRACKER =====")
        print("1. Add Solved Problem")
        print("2. Display All Problems")
        print("3. Search problems")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_problem()
        elif choice == "2":
            display_problems()
        elif choice == "3":
            search_problems()
        elif choice == "4":
            print("THank you for using the tracker!")
            break
        else:
            print("No matching problem found.")
main()