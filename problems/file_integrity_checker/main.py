
import os
import json
import hashlib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_FILE = os.path.join(BASE_DIR, "integrity_records.json")


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("Error: File does not exist.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None


def load_records():
    try:
        with open(RECORD_FILE, "r") as file:
            records = json.load(file)

            if isinstance(records, dict):
                return records

            return {}

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Warning: Integrity records file is corrupted.")
        return {}


def save_records(records):
    with open(RECORD_FILE, "w") as file:
        json.dump(records, file, indent=4)


def generate_file_hash():
    print("\n--- Generate SHA-256 Hash ---")

    file_path = input("Enter file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    if not os.path.isfile(file_path):
        print("Error: Invalid file path.")
        return

    file_hash = calculate_hash(file_path)

    if file_hash:
        print("\nFile:", os.path.basename(file_path))
        print("SHA-256 Hash:", file_hash)


def compare_files():
    print("\n--- Compare Two Files ---")

    file1 = input("Enter first file path: ").strip()
    file2 = input("Enter second file path: ").strip()

    if not file1 or not file2:
        print("File paths cannot be empty.")
        return

    if not os.path.isfile(file1) or not os.path.isfile(file2):
        print("Error: One or both files do not exist.")
        return

    hash1 = calculate_hash(file1)
    hash2 = calculate_hash(file2)

    if hash1 is None or hash2 is None:
        return

    print("\nComparison Result:")

    if hash1 == hash2:
        print("Both files have identical contents.")
    else:
        print("The files have different contents.")


def save_integrity_record(records):
    print("\n--- Save File Integrity Record ---")

    file_path = input("Enter file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return

    file_hash = calculate_hash(file_path)

    if file_hash is None:
        return

    absolute_path = os.path.abspath(file_path)

    records[absolute_path] = file_hash
    save_records(records)

    print("Integrity record saved successfully!")
    print("File:", os.path.basename(file_path))
    print("SHA-256:", file_hash)


def verify_integrity(records):
    print("\n--- Verify File Integrity ---")

    if not records:
        print("No saved integrity records found.")
        return

    print("\nSaved Files:")

    file_list = list(records.keys())

    for index, file_path in enumerate(file_list, start=1):
        print(index, ".", os.path.basename(file_path))

    try:
        number = int(input("\nEnter file number to verify: "))

        if number < 1 or number > len(file_list):
            print("Invalid file number.")
            return

        selected_file = file_list[number - 1]

        if not os.path.isfile(selected_file):
            print("Error: Original file no longer exists.")
            return

        current_hash = calculate_hash(selected_file)

        if current_hash is None:
            return

        saved_hash = records[selected_file]

        if current_hash == saved_hash:
            print("\nFile integrity verified!")
            print("The file has not changed since the record was saved.")
        else:
            print("\nWARNING: File modification detected!")
            print("The current file hash does not match the saved hash.")

    except ValueError:
        print("Please enter a valid number.")


def find_duplicate_files():
    print("\n--- Duplicate File Finder ---")

    folder_path = input("Enter folder path: ").strip()

    if not folder_path:
        print("Folder path cannot be empty.")
        return

    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return

    hash_groups = {}

    for root, directories, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if not os.path.isfile(file_path):
                continue

            file_hash = calculate_hash(file_path)

            if file_hash is not None:
                if file_hash not in hash_groups:
                    hash_groups[file_hash] = []

                hash_groups[file_hash].append(file_path)

    duplicate_count = 0

    print("\nDuplicate Files:")

    for file_paths in hash_groups.values():
        if len(file_paths) > 1:
            duplicate_count += 1

            print("\nDuplicate Group:")

            for file_path in file_paths:
                print("-", file_path)

    if duplicate_count == 0:
        print("No duplicate files found.")
    else:
        print("\nTotal duplicate groups:", duplicate_count)


def main():
    records = load_records()

    while True:
        print("\n========================================")
        print("   FILE INTEGRITY CHECKER & DUPLICATE FINDER")
        print("========================================")
        print("1. Generate SHA-256 hash")
        print("2. Compare two files")
        print("3. Save file integrity record")
        print("4. Verify file integrity")
        print("5. Find duplicate files")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            generate_file_hash()

        elif choice == "2":
            compare_files()

        elif choice == "3":
            save_integrity_record(records)

        elif choice == "4":
            verify_integrity(records)

        elif choice == "5":
            find_duplicate_files()

        elif choice == "6":
            print("Thank you for using File Integrity Checker!")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


main()
