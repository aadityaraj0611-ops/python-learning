
patients = {}
doctors = {}
appointments = {}
bills = {}

next_patient_id = 1001
next_doctor_id = 501
next_appointment_id = 1
next_bill_id = 1


# 1. Register a new patient
def register_patient():
    global next_patient_id

    name = input("Enter patient name: ").strip()

    if name == "":
        print("Patient name cannot be empty!")
        return

    try:
        age = int(input("Enter patient age: "))

        if age <= 0 or age > 120:
            print("Enter a valid age!")
            return

    except ValueError:
        print("Age must be a valid number!")
        return

    gender = input("Enter gender: ").strip()
    phone = input("Enter phone number: ").strip()

    if gender == "" or phone == "":
        print("Gender and phone number cannot be empty!")
        return

    patient_id = next_patient_id
    next_patient_id += 1

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    print("\nPatient registered successfully!")
    print("Patient ID:", patient_id)


# 2. Display all patients
def display_patients():
    if len(patients) == 0:
        print("No patients registered!")
        return

    print("\n----- REGISTERED PATIENTS -----")

    for patient_id, details in patients.items():
        print("\nPatient ID:", patient_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Gender:", details["gender"])
        print("Phone:", details["phone"])


# 3. Search for a patient
def search_patient():
    try:
        patient_id = int(input("Enter patient ID: "))

        if patient_id in patients:
            details = patients[patient_id]

            print("\nPatient Found!")
            print("Patient ID:", patient_id)
            print("Name:", details["name"])
            print("Age:", details["age"])
            print("Gender:", details["gender"])
            print("Phone:", details["phone"])

        else:
            print("Patient does not exist!")

    except ValueError:
        print("Enter a valid patient ID!")


# 4. Register a doctor
def register_doctor():
    global next_doctor_id

    name = input("Enter doctor name: ").strip()

    if name == "":
        print("Doctor name cannot be empty!")
        return

    specialization = input("Enter specialization: ").strip()

    if specialization == "":
        print("Specialization cannot be empty!")
        return

    try:
        consultation_fee = float(input("Enter consultation fee: "))

        if consultation_fee <= 0:
            print("Consultation fee must be greater than zero!")
            return

    except ValueError:
        print("Enter a valid consultation fee!")
        return

    doctor_id = next_doctor_id
    next_doctor_id += 1

    doctors[doctor_id] = {
        "name": name,
        "specialization": specialization,
        "consultation_fee": consultation_fee
    }

    print("\nDoctor registered successfully!")
    print("Doctor ID:", doctor_id)


# 5. Display all doctors
def display_doctors():
    if len(doctors) == 0:
        print("No doctors registered!")
        return

    print("\n----- REGISTERED DOCTORS -----")

    for doctor_id, details in doctors.items():
        print("\nDoctor ID:", doctor_id)
        print("Name:", details["name"])
        print("Specialization:", details["specialization"])
        print("Consultation Fee: ₹", details["consultation_fee"])


# 6. Book an appointment
def book_appointment():
    global next_appointment_id

    try:
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))

        if patient_id not in patients:
            print("Patient does not exist!")
            return

        if doctor_id not in doctors:
            print("Doctor does not exist!")
            return

        appointment_date = input("Enter appointment date (DD-MM-YYYY): ").strip()

        if appointment_date == "":
            print("Appointment date cannot be empty!")
            return

        appointment_time = input("Enter appointment time: ").strip()

        if appointment_time == "":
            print("Appointment time cannot be empty!")
            return

        # Prevent duplicate active appointments
        for appointment in appointments.values():
            if (
                appointment["patient_id"] == patient_id
                and appointment["doctor_id"] == doctor_id
                and appointment["date"] == appointment_date
                and appointment["time"] == appointment_time
                and appointment["status"] == "Booked"
            ):
                print("This appointment is already booked!")
                return

        appointment_id = next_appointment_id
        next_appointment_id += 1

        appointments[appointment_id] = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": appointment_date,
            "time": appointment_time,
            "status": "Booked"
        }

        print("\nAppointment booked successfully!")
        print("Appointment ID:", appointment_id)

    except ValueError:
        print("Enter valid patient and doctor IDs!")


# 7. Display all appointments
def display_appointments():
    if len(appointments) == 0:
        print("No appointments available!")
        return

    print("\n----- APPOINTMENT DETAILS -----")

    for appointment_id, details in appointments.items():
        patient_id = details["patient_id"]
        doctor_id = details["doctor_id"]

        print("\nAppointment ID:", appointment_id)
        print("Patient:", patients[patient_id]["name"])
        print("Doctor:", doctors[doctor_id]["name"])
        print("Date:", details["date"])
        print("Time:", details["time"])
        print("Status:", details["status"])


# 8. Cancel an appointment
def cancel_appointment():
    try:
        appointment_id = int(input("Enter appointment ID: "))

        if appointment_id not in appointments:
            print("Appointment does not exist!")
            return

        if appointments[appointment_id]["status"] == "Cancelled":
            print("Appointment is already cancelled!")
            return

        appointments[appointment_id]["status"] = "Cancelled"

        print("Appointment cancelled successfully!")

    except ValueError:
        print("Enter a valid appointment ID!")


# 9. Generate patient bill
def generate_bill():
    global next_bill_id

    try:
        patient_id = int(input("Enter patient ID: "))

        if patient_id not in patients:
            print("Patient does not exist!")
            return

        doctor_id = int(input("Enter doctor ID: "))

        if doctor_id not in doctors:
            print("Doctor does not exist!")
            return

        try:
            treatment_charge = float(input("Enter treatment charges: "))

            if treatment_charge < 0:
                print("Treatment charges cannot be negative!")
                return

        except ValueError:
            print("Enter valid treatment charges!")
            return

        consultation_fee = doctors[doctor_id]["consultation_fee"]
        total_bill = consultation_fee + treatment_charge

        bill_id = next_bill_id
        next_bill_id += 1

        bills[bill_id] = {
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "consultation_fee": consultation_fee,
            "treatment_charge": treatment_charge,
            "total_bill": total_bill
        }

        print("\n========== PATIENT BILL ==========")
        print("Bill ID:", bill_id)
        print("Patient:", patients[patient_id]["name"])
        print("Doctor:", doctors[doctor_id]["name"])
        print("Consultation Fee: ₹", consultation_fee)
        print("Treatment Charges: ₹", treatment_charge)
        print("----------------------------------")
        print("Total Bill: ₹", total_bill)
        print("==================================")

    except ValueError:
        print("Enter valid patient and doctor IDs!")


# 10. View patient history
def patient_history():
    try:
        patient_id = int(input("Enter patient ID: "))

        if patient_id not in patients:
            print("Patient does not exist!")
            return

        print("\n========== PATIENT HISTORY ==========")
        print("Patient:", patients[patient_id]["name"])

        found_appointment = False
        found_bill = False

        print("\n----- APPOINTMENTS -----")

        for appointment_id, details in appointments.items():
            if details["patient_id"] == patient_id:
                found_appointment = True

                print("Appointment ID:", appointment_id)
                print("Doctor:", doctors[details["doctor_id"]]["name"])
                print("Date:", details["date"])
                print("Time:", details["time"])
                print("Status:", details["status"])

        if not found_appointment:
            print("No appointment history found.")

        print("\n----- BILLS -----")

        for bill_id, details in bills.items():
            if details["patient_id"] == patient_id:
                found_bill = True

                print("Bill ID:", bill_id)
                print("Doctor:", doctors[details["doctor_id"]]["name"])
                print("Total Bill: ₹", details["total_bill"])

        if not found_bill:
            print("No bills found.")

    except ValueError:
        print("Enter a valid patient ID!")


# 11. Calculate hospital revenue
def calculate_revenue():
    total_revenue = 0

    for details in bills.values():
        total_revenue += details["total_bill"]

    print("Total Hospital Revenue: ₹", total_revenue)


# Main menu
def main():
    while True:
        print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")
        print("1. Register Patient")
        print("2. Display All Patients")
        print("3. Search Patient")
        print("4. Register Doctor")
        print("5. Display All Doctors")
        print("6. Book Appointment")
        print("7. Display All Appointments")
        print("8. Cancel Appointment")
        print("9. Generate Patient Bill")
        print("10. View Patient History")
        print("11. Calculate Hospital Revenue")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            display_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            register_doctor()

        elif choice == "5":
            display_doctors()

        elif choice == "6":
            book_appointment()

        elif choice == "7":
            display_appointments()

        elif choice == "8":
            cancel_appointment()

        elif choice == "9":
            generate_bill()

        elif choice == "10":
            patient_history()

        elif choice == "11":
            calculate_revenue()

        elif choice == "12":
            print("Thank you for using Hospital Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
