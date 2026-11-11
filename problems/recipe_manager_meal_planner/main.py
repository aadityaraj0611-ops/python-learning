
import json
import os

DATA_FILE = "recipes.json"

CATEGORIES = ["Breakfast", "Lunch", "Dinner", "Snacks"]


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"recipes": [], "meal_plan": {}}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        if "recipes" not in data or "meal_plan" not in data:
            print("Invalid data file. Starting with empty data.")
            return {"recipes": [], "meal_plan": {}}

        return data

    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with empty data.")
        return {"recipes": [], "meal_plan": {}}


def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save data.")
        return False


def get_recipe_by_name(recipes, name):
    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            return recipe

    return None


def add_recipe(data):
    print("\n--- Add New Recipe ---")

    name = input("Enter recipe name: ").strip()

    if not name:
        print("Recipe name cannot be empty.")
        return

    if get_recipe_by_name(data["recipes"], name):
        print("A recipe with this name already exists.")
        return

    ingredients_input = input(
        "Enter ingredients separated by commas: "
    ).strip()

    ingredients = []

    for ingredient in ingredients_input.split(","):
        ingredient = ingredient.strip()

        if ingredient and ingredient.lower() not in [
            item.lower() for item in ingredients
        ]:
            ingredients.append(ingredient)

    if not ingredients:
        print("You must enter at least one ingredient.")
        return

    try:
        cooking_time = int(input("Enter cooking time in minutes: "))

        if cooking_time <= 0:
            print("Cooking time must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number for cooking time.")
        return

    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Choose category number: "))

        if category_choice < 1 or category_choice > len(CATEGORIES):
            print("Invalid category choice.")
            return

    except ValueError:
        print("Please enter a valid category number.")
        return

    category = CATEGORIES[category_choice - 1]

    instructions = input("Enter cooking instructions: ").strip()

    if not instructions:
        print("Instructions cannot be empty.")
        return

    recipe = {
        "name": name,
        "ingredients": ingredients,
        "cooking_time": cooking_time,
        "category": category,
        "instructions": instructions
    }

    data["recipes"].append(recipe)

    if save_data(data):
        print(f"\nRecipe '{name}' added successfully!")


def view_recipes(data):
    print("\n--- All Recipes ---")

    if not data["recipes"]:
        print("No recipes found.")
        return

    for index, recipe in enumerate(data["recipes"], start=1):
        print(f"\nRecipe {index}")
        print(f"Name: {recipe['name']}")
        print(f"Category: {recipe['category']}")
        print(f"Cooking Time: {recipe['cooking_time']} minutes")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")


def search_recipes(data):
    print("\n--- Search Recipes ---")

    search_term = input(
        "Enter recipe name or ingredient: "
    ).strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found_recipes = []

    for recipe in data["recipes"]:
        name_match = search_term in recipe["name"].lower()

        ingredient_match = False

        for ingredient in recipe["ingredients"]:
            if search_term in ingredient.lower():
                ingredient_match = True
                break

        if name_match or ingredient_match:
            found_recipes.append(recipe)

    if not found_recipes:
        print("No matching recipes found.")
        return

    print("\nMatching Recipes:")

    for recipe in found_recipes:
        print(f"\nName: {recipe['name']}")
        print(f"Category: {recipe['category']}")
        print(f"Cooking Time: {recipe['cooking_time']} minutes")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")


def update_recipe(data):
    print("\n--- Update Recipe ---")

    name = input("Enter the recipe name to update: ").strip()

    recipe = get_recipe_by_name(data["recipes"], name)

    if recipe is None:
        print("Recipe not found.")
        return

    print("\nLeave a field empty to keep its current value.")

    new_name = input(
        f"New name [{recipe['name']}]: "
    ).strip()

    if new_name:
        existing_recipe = get_recipe_by_name(data["recipes"], new_name)

        if existing_recipe and existing_recipe != recipe:
            print("Another recipe already uses this name.")
            return

        recipe["name"] = new_name

    new_ingredients = input(
        "New ingredients separated by commas: "
    ).strip()

    if new_ingredients:
        ingredients = []

        for ingredient in new_ingredients.split(","):
            ingredient = ingredient.strip()

            if ingredient and ingredient.lower() not in [
                item.lower() for item in ingredients
            ]:
                ingredients.append(ingredient)

        if not ingredients:
            print("At least one ingredient is required.")
            return

        recipe["ingredients"] = ingredients

    new_time = input(
        f"New cooking time [{recipe['cooking_time']}]: "
    ).strip()

    if new_time:
        try:
            cooking_time = int(new_time)

            if cooking_time <= 0:
                print("Cooking time must be greater than zero.")
                return

            recipe["cooking_time"] = cooking_time

        except ValueError:
            print("Invalid cooking time.")
            return

    print("\nAvailable Categories:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    new_category = input(
        f"New category number (current: {recipe['category']}): "
    ).strip()

    if new_category:
        try:
            category_choice = int(new_category)

            if category_choice < 1 or category_choice > len(CATEGORIES):
                print("Invalid category choice.")
                return

            recipe["category"] = CATEGORIES[category_choice - 1]

        except ValueError:
            print("Invalid category number.")
            return

    new_instructions = input("New instructions: ").strip()

    if new_instructions:
        recipe["instructions"] = new_instructions

    if save_data(data):
        print("Recipe updated successfully!")


def delete_recipe(data):
    print("\n--- Delete Recipe ---")

    name = input("Enter recipe name to delete: ").strip()

    recipe = get_recipe_by_name(data["recipes"], name)

    if recipe is None:
        print("Recipe not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{recipe['name']}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        data["recipes"].remove(recipe)

        for day in data["meal_plan"]:
            for meal in list(data["meal_plan"][day]):
                if data["meal_plan"][day][meal].lower() == name.lower():
                    del data["meal_plan"][day][meal]

        if save_data(data):
            print("Recipe deleted successfully!")
    else:
        print("Deletion cancelled.")


def view_categories(data):
    print("\n--- Recipes by Category ---")

    for category in CATEGORIES:
        print(f"\n{category}:")

        found = False

        for recipe in data["recipes"]:
            if recipe["category"] == category:
                print(f"- {recipe['name']}")
                found = True

        if not found:
            print("No recipes in this category.")


def add_meal_plan(data):
    print("\n--- Weekly Meal Planner ---")

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    for index, day in enumerate(days, start=1):
        print(f"{index}. {day}")

    try:
        day_choice = int(input("Choose a day number: "))

        if day_choice < 1 or day_choice > len(days):
            print("Invalid day choice.")
            return

    except ValueError:
        print("Please enter a valid day number.")
        return

    day = days[day_choice - 1]

    print("\n1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Snacks")

    try:
        meal_choice = int(input("Choose meal type: "))

        if meal_choice < 1 or meal_choice > len(CATEGORIES):
            print("Invalid meal choice.")
            return

    except ValueError:
        print("Please enter a valid meal number.")
        return

    meal = CATEGORIES[meal_choice - 1]

    recipe_name = input("Enter recipe name: ").strip()

    recipe = get_recipe_by_name(data["recipes"], recipe_name)

    if recipe is None:
        print("Recipe not found. Add the recipe first.")
        return

    if day not in data["meal_plan"]:
        data["meal_plan"][day] = {}

    data["meal_plan"][day][meal] = recipe["name"]

    if save_data(data):
        print(f"{recipe['name']} added to {day} - {meal}!")


def view_meal_plan(data):
    print("\n--- Weekly Meal Plan ---")

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    for day in days:
        print(f"\n{day}:")

        if day not in data["meal_plan"] or not data["meal_plan"][day]:
            print("  No meals planned.")
            continue

        for meal, recipe_name in data["meal_plan"][day].items():
            print(f"  {meal}: {recipe_name}")


def main():
    data = load_data()

    while True:
        print("\n========== RECIPE MANAGER & MEAL PLANNER ==========")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipes")
        print("4. Update Recipe")
        print("5. Delete Recipe")
        print("6. View Recipes by Category")
        print("7. Add Recipe to Weekly Meal Plan")
        print("8. View Weekly Meal Plan")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_recipe(data)

        elif choice == "2":
            view_recipes(data)

        elif choice == "3":
            search_recipes(data)

        elif choice == "4":
            update_recipe(data)

        elif choice == "5":
            delete_recipe(data)

        elif choice == "6":
            view_categories(data)

        elif choice == "7":
            add_meal_plan(data)

        elif choice == "8":
            view_meal_plan(data)

        elif choice == "9":
            print("\nThank you for using Recipe Manager!")
            break

        else:
            print("Invalid choice. Please select between 1 and 9.")


if __name__ == "__main__":
    main()
