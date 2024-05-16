def calculate_adjustment_factor(original_servings, desired_servings):
    return desired_servings / original_servings

def main():
    # Recipe ingredients for 12 cookies
    original_ingredients = {
        "chocolate_chips": 0.5,  # 1/2 cup chocolate chips
        "peanut_butter": 0.5,    # 1/2 cup natural creamy peanut butter
        "rolled_oats": 1.5       # 1 1/2 cups rolled oats
    }

    while True: #Task 1
        try:
            original_servings = float(input("Enter the number of servings the recipe is originally for: "))
            desired_servings = float(input("Enter the number of servings you wish to make: "))
            break  # Break out of the loop if inputs are valid
        except ValueError:
            print("Error: Please enter valid numbers for the servings.")

    try: #Task 2
        adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
        adjusted_ingredients = {ingredient: quantity * adjustment_factor for ingredient, quantity in original_ingredients.items()}
    except ZeroDivisionError:
        print("Error: The number of original servings cannot be zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Adjusted Recipe Ingredients:")
        for ingredient, quantity in adjusted_ingredients.items():
            print(f"{ingredient.capitalize()}: {quantity:.2f} cups")
    finally: #Task 3
        print("Enjoy your cooking!")

if __name__ == "__main__":
    main()
