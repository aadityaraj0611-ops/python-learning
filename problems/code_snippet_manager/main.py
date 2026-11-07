
import json
import os


FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "snippets.json"
)


def load_snippets():
    try:
        with open(FILE_NAME, "r") as file:
            snippets = json.load(file)

            if isinstance(snippets, list):
                return snippets

            return []

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: Snippet file is corrupted. Starting with an empty list.")
        return []


def save_snippets(snippets):
    with open(FILE_NAME, "w") as file:
        json.dump(snippets, file, indent=4)


def add_snippet(snippets):
    print("\n--- Add New Snippet ---")

    title = input("Enter snippet title: ").strip()
    language = input("Enter programming language: ").strip()
    description = input("Enter description: ").strip()
    code = input("Enter code snippet: ").strip()

    if not title or not language or not code:
        print("Title, language, and code cannot be empty.")
        return

    snippet = {
        "title": title,
        "language": language,
        "description": description,
        "code": code
    }

    snippets.append(snippet)
    save_snippets(snippets)

    print("Snippet added successfully!")


def view_snippets(snippets):
    print("\n--- All Code Snippets ---")

    if not snippets:
        print("No snippets available.")
        return

    for index, snippet in enumerate(snippets, start=1):
        print("\nSnippet Number:", index)
        print("Title:", snippet["title"])
        print("Language:", snippet["language"])
        print("Description:", snippet["description"])
        print("Code:")
        print(snippet["code"])
        print("-" * 40)


def search_snippets(snippets):
    print("\n--- Search Snippets ---")

    keyword = input("Enter title or language to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False

    for index, snippet in enumerate(snippets, start=1):
        if (
            keyword in snippet["title"].lower()
            or keyword in snippet["language"].lower()
        ):
            print("\nSnippet Number:", index)
            print("Title:", snippet["title"])
            print("Language:", snippet["language"])
            print("Description:", snippet["description"])
            print("Code:")
            print(snippet["code"])
            print("-" * 40)
            found = True

    if not found:
        print("No matching snippets found.")


def update_snippet(snippets):
    print("\n--- Update Snippet ---")

    if not snippets:
        print("No snippets available to update.")
        return

    view_snippets(snippets)

    try:
        number = int(input("Enter snippet number to update: "))

        if number < 1 or number > len(snippets):
            print("Invalid snippet number.")
            return

        snippet = snippets[number - 1]

        print("\nPress Enter to keep the existing value.")

        title = input("New title: ").strip()
        language = input("New language: ").strip()
        description = input("New description: ").strip()
        code = input("New code: ").strip()

        if title:
            snippet["title"] = title

        if language:
            snippet["language"] = language

        if description:
            snippet["description"] = description

        if code:
            snippet["code"] = code

        save_snippets(snippets)

        print("Snippet updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def delete_snippet(snippets):
    print("\n--- Delete Snippet ---")

    if not snippets:
        print("No snippets available to delete.")
        return

    view_snippets(snippets)

    try:
        number = int(input("Enter snippet number to delete: "))

        if number < 1 or number > len(snippets):
            print("Invalid snippet number.")
            return

        removed = snippets.pop(number - 1)

        save_snippets(snippets)

        print("Deleted snippet:", removed["title"])

    except ValueError:
        print("Please enter a valid number.")


def show_languages(snippets):
    print("\n--- Programming Languages ---")

    if not snippets:
        print("No snippets available.")
        return

    languages = set()

    for snippet in snippets:
        languages.add(snippet["language"])

    print("Total languages:", len(languages))

    for language in sorted(languages):
        count = 0

        for snippet in snippets:
            if snippet["language"].lower() == language.lower():
                count += 1

        print(language, "-", count, "snippet(s)")


def main():
    snippets = load_snippets()

    while True:
        print("\n================================")
        print("       CODE SNIPPET MANAGER")
        print("================================")
        print("1. Add a snippet")
        print("2. View all snippets")
        print("3. Search snippets")
        print("4. Update a snippet")
        print("5. Delete a snippet")
        print("6. View programming languages")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_snippet(snippets)

        elif choice == "2":
            view_snippets(snippets)

        elif choice == "3":
            search_snippets(snippets)

        elif choice == "4":
            update_snippet(snippets)

        elif choice == "5":
            delete_snippet(snippets)

        elif choice == "6":
            show_languages(snippets)

        elif choice == "7":
            print("Thank you for using Code Snippet Manager!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


main()
