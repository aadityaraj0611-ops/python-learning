
import csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(BASE_DIR, "sample_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "cleaned_data.csv")
REPORT_FILE = os.path.join(BASE_DIR, "cleaning_report.txt")


def read_csv_file():
    """Read records from the input CSV file."""
    try:
        with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV file is empty or has no headers.")
                return None

            headers = reader.fieldnames
            records = list(reader)

            if not records:
                print("The CSV file contains no records.")
                return None

            return headers, records

    except FileNotFoundError:
        print("Error: Sample CSV file not found.")
        return None

    except (OSError, csv.Error, UnicodeDecodeError) as error:
        print(f"Error reading CSV file: {error}")
        return None


def display_records(headers, records):
    """Display CSV records."""
    if not records:
        print("\nNo records available.")
        return

    print("\n" + "-" * 80)
    print(" | ".join(headers))
    print("-" * 80)

    for record in records:
        print(" | ".join(str(record.get(header, "")) for header in headers))

    print("-" * 80)
    print(f"Total records: {len(records)}")


def detect_missing_values(headers, records):
    """Count missing values in each column."""
    print("\n========== MISSING VALUE ANALYSIS ==========")

    total_missing = 0

    for header in headers:
        count = 0

        for record in records:
            if not record.get(header, "").strip():
                count += 1

        total_missing += count
        print(f"{header:<15}: {count} missing value(s)")

    print("--------------------------------------------")
    print(f"Total missing values: {total_missing}")


def detect_duplicates(records):
    """Identify duplicate records."""
    seen_records = set()
    duplicate_records = []

    for index, record in enumerate(records):
        record_key = tuple(record.values())

        if record_key in seen_records:
            duplicate_records.append(index)

        else:
            seen_records.add(record_key)

    print("\n========== DUPLICATE RECORD ANALYSIS ==========")

    if not duplicate_records:
        print("No duplicate records found.")

    else:
        for index in duplicate_records:
            print(f"Duplicate record found at row {index + 1} (excluding header).")

        print(f"Total duplicate records: {len(duplicate_records)}")

    return duplicate_records


def clean_records(headers, records):
    """Remove duplicate rows and fill missing values."""
    cleaned_records = []
    seen_records = set()

    removed_duplicates = 0
    filled_values = 0

    for record in records:
        record_key = tuple(record.values())

        if record_key in seen_records:
            removed_duplicates += 1
            continue

        seen_records.add(record_key)

        cleaned_record = {}

        for header in headers:
            value = record.get(header, "").strip()

            if value == "":
                value = "Unknown"
                filled_values += 1

            cleaned_record[header] = value

        cleaned_records.append(cleaned_record)

    print("\n========== DATA CLEANING ==========")
    print(f"Original records       : {len(records)}")
    print(f"Duplicate records removed: {removed_duplicates}")
    print(f"Missing values filled  : {filled_values}")
    print(f"Final records          : {len(cleaned_records)}")

    return cleaned_records, removed_duplicates, filled_values


def analyze_numeric_columns(headers, records):
    """Calculate statistics for numeric columns."""
    print("\n========== NUMERIC COLUMN ANALYSIS ==========")

    numeric_columns_found = False

    for header in headers:
        numbers = []

        for record in records:
            value = record.get(header, "").strip()

            if value == "" or value.lower() == "unknown":
                continue

            try:
                numbers.append(float(value))

            except ValueError:
                numbers = []
                break

        if numbers:
            numeric_columns_found = True

            average = sum(numbers) / len(numbers)

            print(f"\nColumn: {header}")
            print(f"Count   : {len(numbers)}")
            print(f"Minimum : {min(numbers):g}")
            print(f"Maximum : {max(numbers):g}")
            print(f"Average : {average:.2f}")

    if not numeric_columns_found:
        print("No numeric columns found.")


def save_cleaned_data(headers, records):
    """Save cleaned records into a new CSV file."""
    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            writer.writeheader()
            writer.writerows(records)

        print(f"\nCleaned data saved to: {OUTPUT_FILE}")

        return True

    except (OSError, csv.Error) as error:
        print(f"Error saving cleaned data: {error}")
        return False


def generate_report(original_records, cleaned_records,
                    removed_duplicates, filled_values):
    """Generate a text report of the cleaning process."""
    total_missing = 0

    for record in original_records:
        for value in record.values():
            if not value.strip():
                total_missing += 1

    try:
        with open(REPORT_FILE, "w", encoding="utf-8") as file:
            file.write("========== CSV DATA CLEANING REPORT ==========\n\n")

            file.write(f"Original records: {len(original_records)}\n")
            file.write(f"Final records: {len(cleaned_records)}\n")
            file.write(f"Original missing values: {total_missing}\n")
            file.write(f"Duplicate records removed: {removed_duplicates}\n")
            file.write(f"Missing values filled: {filled_values}\n")

            file.write(
                f"Records removed: {len(original_records) - len(cleaned_records)}\n"
            )

            file.write("\nCleaning completed successfully.\n")

        print(f"Cleaning report saved to: {REPORT_FILE}")

    except OSError as error:
        print(f"Error generating report: {error}")


def main():
    data = read_csv_file()

    if data is None:
        return

    headers, records = data

    while True:
        print("\n========== CSV DATA CLEANER & ANALYZER ==========")
        print("1. Display original CSV records")
        print("2. Detect missing values")
        print("3. Detect duplicate records")
        print("4. Analyze numeric columns")
        print("5. Clean and save CSV data")
        print("6. Generate cleaning report")
        print("7. Exit")
        print("=================================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            display_records(headers, records)

        elif choice == "2":
            detect_missing_values(headers, records)

        elif choice == "3":
            detect_duplicates(records)

        elif choice == "4":
            analyze_numeric_columns(headers, records)

        elif choice == "5":
            cleaned_records, removed, filled = clean_records(
                headers, records
            )

            if save_cleaned_data(headers, cleaned_records):
                records = cleaned_records

        elif choice == "6":
            cleaned_records, removed, filled = clean_records(
                headers, records
            )

            generate_report(records, cleaned_records, removed, filled)

        elif choice == "7":
            print("\nThank you for using CSV Data Cleaner & Analyzer!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()
