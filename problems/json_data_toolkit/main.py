
import json
import os


def load_json_file(file_path):
    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        print("Invalid JSON file.")
        print("Error:", error)
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    except UnicodeDecodeError:
        print("Error: Unable to read file encoding.")
        return None


def validate_json():
    print("\n--- JSON Validator ---")

    file_path = input("Enter JSON file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    data = load_json_file(file_path)

    if data is not None:
        print("Valid JSON file!")
    elif os.path.isfile(file_path):
        print("JSON validation failed.")


def format_json():
    print("\n--- JSON Formatter ---")

    file_path = input("Enter JSON file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    data = load_json_file(file_path)

    if data is None:
        return

    formatted_data = json.dumps(data, indent=4, ensure_ascii=False)

    output_path = os.path.splitext(file_path)[0] + "_formatted.json"

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(formatted_data)

        print("JSON formatted successfully!")
        print("Output file:", output_path)

    except PermissionError:
        print("Error: Permission denied while writing the file.")


def minify_json():
    print("\n--- JSON Minifier ---")

    file_path = input("Enter JSON file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    data = load_json_file(file_path)

    if data is None:
        return

    minified_data = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

    output_path = os.path.splitext(file_path)[0] + "_minified.json"

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(minified_data)

        print("JSON minified successfully!")
        print("Output file:", output_path)

    except PermissionError:
        print("Error: Permission denied while writing the file.")


def view_json():
    print("\n--- JSON Viewer ---")

    file_path = input("Enter JSON file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    data = load_json_file(file_path)

    if data is None:
        return

    print("\nJSON Data:")
    print(json.dumps(data, indent=4, ensure_ascii=False))


def compare_json():
    print("\n--- JSON File Comparator ---")

    file1 = input("Enter first JSON file path: ").strip()
    file2 = input("Enter second JSON file path: ").strip()

    if not file1 or not file2:
        print("File paths cannot be empty.")
        return

    data1 = load_json_file(file1)
    if data1 is None:
        return

    data2 = load_json_file(file2)
    if data2 is None:
        return

    if data1 == data2:
        print("Both JSON files contain identical data.")
    else:
        print("The JSON files contain different data.")


def search_keys(data, target_key, current_path=""):
    results = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_path = current_path + "." + key if current_path else key

            if key.lower() == target_key.lower():
                results.append((new_path, value))

            results.extend(search_keys(value, target_key, new_path))

    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_path = f"{current_path}[{index}]"
            results.extend(search_keys(value, target_key, new_path))

    return results


def find_json_key():
    print("\n--- JSON Key Finder ---")

    file_path = input("Enter JSON file path: ").strip()

    if not file_path:
        print("File path cannot be empty.")
        return

    data = load_json_file(file_path)

    if data is None:
        return

    target_key = input("Enter key to search: ").strip()

    if not target_key:
        print("Search key cannot be empty.")
        return

    results = search_keys(data, target_key)

    if results:
        print("\nMatching Keys:")

        for path, value in results:
            print("Path:", path)
            print("Value:", json.dumps(value, ensure_ascii=False))
            print("-" * 30)

        print("Total matches:", len(results))

    else:
        print("Key not found.")


def main():
    while True:
        print("\n================================")
        print("         JSON DATA TOOLKIT")
        print("================================")
        print("1. Validate JSON file")
        print("2. Format JSON file")
        print("3. Minify JSON file")
        print("4. View JSON data")
        print("5. Compare two JSON files")
        print("6. Find a JSON key")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            validate_json()

        elif choice == "2":
            format_json()

        elif choice == "3":
            minify_json()

        elif choice == "4":
            view_json()

        elif choice == "5":
            compare_json()

        elif choice == "6":
            find_json_key()

        elif choice == "7":
            print("Thank you for using JSON Data Toolkit!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


main()
