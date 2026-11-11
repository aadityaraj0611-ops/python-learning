# Recipe Manager & Meal Planner

## Project Overview

The **Recipe Manager & Meal Planner** is a menu-driven Python application that helps users organize their recipes and plan meals throughout the week.

Users can add, view, search, update, and delete recipes, organize them into categories, and assign recipes to different days and meals using a weekly meal planner.

The application stores data in a JSON file, allowing recipes and meal plans to remain available even after the program is closed.

## Features

- **Add Recipes:** Store recipes with names, ingredients, cooking time, categories, and instructions.
- **View Recipes:** Display all saved recipes and their details.
- **Search Recipes:** Search recipes using their names or ingredients.
- **Update Recipes:** Modify existing recipe information.
- **Delete Recipes:** Remove recipes from the collection.
- **Category Management:** Organize recipes into Breakfast, Lunch, Dinner, and Snacks.
- **Weekly Meal Planner:** Assign recipes to specific days and meal categories.
- **View Weekly Plan:** Display the complete weekly meal schedule.
- **Data Persistence:** Automatically save and retrieve information using JSON.
- **Input Validation:** Handle invalid choices and incorrect user inputs.

## Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Modules:** `json`, `os`

## Python Concepts Practiced

This project demonstrates practical use of:

- Variables and data types
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for` and `while`)
- Functions
- Lists and dictionaries
- Nested dictionaries
- String manipulation
- File handling
- JSON serialization and deserialization
- Exception handling (`try`, `except`)
- List operations and searching

## Project Structure

```text
recipe_manager_meal_planner/
│
├── main.py
├── README.md
└── recipes.json
```

**Note:** `recipes.json` is generated automatically when the application successfully saves its first recipe.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/aadityaraj0611-ops/python-learning.git
```

### 2. Navigate to the Project Directory

```bash
cd python-learning/problems/recipe_manager_meal_planner
```

### 3. Run the Application

```bash
python3 main.py
```

No external Python packages are required.

## Application Menu

```text
========== RECIPE MANAGER & MEAL PLANNER ==========

1. Add Recipe
2. View All Recipes
3. Search Recipes
4. Update Recipe
5. Delete Recipe
6. View Recipes by Category
7. Add Recipe to Weekly Meal Plan
8. View Weekly Meal Plan
9. Exit

Enter your choice:
```

## Available Recipe Categories

1. Breakfast
2. Lunch
3. Dinner
4. Snacks

## Weekly Meal Planner

The application supports meal planning for all seven days:

- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

Each day can have a separate recipe assigned to Breakfast, Lunch, Dinner, and Snacks.

## Data Storage

All recipe information and weekly meal plans are stored in `recipes.json`.

The application uses Python's built-in JSON module to:

- Save recipe information.
- Retrieve previously saved recipes.
- Update existing records.
- Maintain weekly meal plans.
- Preserve data between program executions.

## Learning Outcomes

Through this project, I practiced building a complete menu-driven Python application, managing structured data using lists and dictionaries, implementing CRUD operations, handling files using JSON, and organizing information through functions.

It also helped strengthen my understanding of how Python fundamentals can be applied to solve practical problems.

## Author

**Aditya Raj**

