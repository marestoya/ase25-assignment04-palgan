def get_sample_meals():
    """
    Returns a list of meals with sample data.
    """
    return [
        {
            "name": "Couscous Salad",
            "category": "Vegetarian",
            "ingredients": ["Couscous", "Cherry tomatoes", "Feta cheese", "Cucumber"]
        },
        {
            "name": "Teriyaki Salmon",
            "category": "Pescatarian",
            "ingredients": ["Salmon", "Teriyaki sauce", "Rice", "Broccoli"]
        },
        {
            "name": "Gluten-Free Pancakes",
            "category": "Gluten-Free",
            "ingredients": ["Gluten-free flour", "Eggs", "Milk"]
        },
        {
            "name": "Lasagna",
            "category": "Quick Meal",
            "ingredients": ["Lasagna pasta", "Tomato sauce", "Minced meat", "Cheese"]
        },
        {
            "name": "Tomato Soup",
            "category": "Quick Meal",
            "ingredients": ["Tomatoes", "Onions", "Garlic", "Vegetable broth"]
        },
        {
            "name": "Salmon Fried Rice",
            "category": "Pescatarian",
            "ingredients": ["Salmon", "Rice", "Onions", "Garlic", "Soy sauce"]
        }
    ]


def display_meals(meals):
    """
    Displays meals to the user
    """
    if not meals:
        print("\nNo meals found.\n")
        return

    for index, meal in enumerate(meals, start=1):
        print(f"{index}. {meal['name']} ({meal['category']})")
        print(f"   Ingredients: {', '.join(meal['ingredients'])}\n")


def search_meals(meals, search_type, query):
    """
    Filters meals by name, ingredient, or category
    """
    query = query.lower()

    if search_type == "name":
        return [meal for meal in meals if query in meal["name"].lower()]

    if search_type == "category":
        return [meal for meal in meals if query in meal["category"].lower()]

    if search_type == "ingredient":
        return [
            meal for meal in meals
            if any(query in ingredient.lower() for ingredient in meal["ingredients"])
        ]

    return []


def main():
    meals = get_sample_meals()
    continue_browsing = True

    while continue_browsing:
        print("\nAvailable Meals:\n")
        display_meals(meals)

        print("Search meals by:")
        print("1 - Name")
        print("2 - Ingredient")
        print("3 - Category")
        print("0 - Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "0":
            break

        search_map = {
            "1": "name",
            "2": "ingredient",
            "3": "category"
        }

        if choice not in search_map:
            print("Invalid choice! Please enter 1, 2, 3, or 0")
        else:
            query = input("Enter search term: ").strip()
            results = search_meals(meals, search_map[choice], query)

            print("\nSearch Results:\n")
            display_meals(results)

        # Ask if the user wants to continue browsing
        while True:
            user_choice = input("Do you want to continue browsing? (y/n): ").strip().lower()
            if user_choice in ("y", "n"):
                break
            print("Invalid input! Please enter 'y' or 'n'")

        if user_choice == "n":
            continue_browsing = False

    print("Goodbye!")

if __name__ == "__main__":
    main()