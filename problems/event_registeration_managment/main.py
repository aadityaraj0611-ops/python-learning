def register_participant(participants):
    roll = input("Enter participant roll number: ")

    if roll in participants:
        print("This roll number is already registered!")
        return

    name = input("Enter participant name: ")
    event = input("Enter event name: ")

    participants[roll] = {
        "name": name,
        "event": event 
    }
    print("Registeration successful!")
def display_prticipants(participants):
    if len(participants) == 0:
        print("No participants registered.")
        return
    print("\n========== REGISTERED PARTICIPANTS ==========")

    for roll, details in participants.items():
        print("\nROll Number:", roll)
        print("Name:", details["name"])
        print("Event:", details["event"])
def search_participant(participants):
    roll = input("Enter roll number to search: ")

    if roll in participants:
        print("\nParticipant Found!")
        print("Roll Number: ", roll)
        print("Name:", participants[roll]["name"])
        print("Event:", participants[roll]["event"])
    else:
        print("Participant not found!")
def cancel_registeration(participants):
    roll = input("Enter roll number to cancel registeration: ")

    if roll in participants:
        print("Registeration cancelled for: ",
              participants[roll]["name"])
        del participants[roll]
    else:
        print("Participants not found")
def count_registerations(participants):
    print("Total registeration:", len(participants))
def display_event_wise(particpants):
    if len(particpants) == 0:
        print("No registeration available.")
        return
    event_names = []

    for details in particpants.values():
        event = details["event"]

        if event not in event_names:
            event_names.append(event)
    print("\n========== EVENT-WISE REGISTERATION ==========")

    for event in event_names:
        print("\nEvent:", event)
        count = 0

        for roll, details in particpants.items():
            if details["event"].lower() == event.lower():
                print("Roll:", roll, "| Name:", details["name"])
                count += 1
        print("Total participants:", count)
def main():
    participants = {}

    while True:
        print("\n===== EVENT REGISTERATION SYSTEM =====")
        print("1. Register Participant")
        print("2. Display All Participants")
        print("3. Search Participant")
        print("4. Cancel Registeration")
        print("5. Total Registerations")
        print("6. Display Event-wise Registerations")
        print("7. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                register_participant(participants)
            elif choice == 2:
                display_prticipants(participants)
            elif choice == 3:
                search_participant(participants)
            elif choice == 4:
                cancel_registeration(participants)
            elif choice == 5:
                count_registerations(participants)
            elif choice == 6:
                display_event_wise(participants)
            elif choice == 7:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Select between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter a number.")
main()