def calculate_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    total_months = years * 12

    if annual_rate == 0:
        emi = principal / total_months
    else:
        rate_factor = (1 + monthly_rate) ** total_months
        emi = (principal * monthly_rate * rate_factor) / (rate_factor - 1)
        return emi

print("===== Loan EMI Calculator =====")

while True:
    try:
        loan_amount = float(input("Enter loan amount (₹): "))

        if loan_amount < 0:
            print("Loan amount must be greater than zero.")
            continue
        break
    except ValueError:
        print("Please enter a valid numeric loan amount.")

while True:
    try:
        annual_interest_rate = float(
            input("Enter annual interest rate (%): ")
        )

        if annual_interest_rate < 0:
            print("Interest rate cannot be negative.")
            continue
        break
    except ValueError:
        print("Please enter a valid numeric interest rate.")

while True:
    try:
        loan_duration_years = int(
            input("Enter loan duration (years): ")
        )

        if loan_duration_years <= 0:
            print("Loan duration must be at least 1 year.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number of years.")

monthly_emi = calculate_emi(
    loan_amount,
    annual_interest_rate,
    loan_duration_years
)

total_months = loan_duration_years * 12
total_payment = monthly_emi * total_months
total_interest = total_payment - loan_amount

print("\n===== Loan Repayment Summary =====")
print("Loan Amount: ₹", round(loan_amount, 2))
print("Annual Interest Rate:", annual_interest_rate, "%")
print("Loan Duration:", loan_duration_years, "years")
print("Number of Monthly Payments:", total_months)
print("Monthly EMI: ₹", round(monthly_emi, 2))
print("Total Repayment: ₹", round(total_payment, 2))
print("Total Interest Payable: ₹", round(total_interest, 2))