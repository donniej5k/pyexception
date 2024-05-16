# def for Task 2
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        user_input = input("Please enter the temperature in Fahrenheit (or type 'exit' to quit): ") # Task 1

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:    # Task 2
            fahrenheit = float(user_input)
            celsius = fahrenheit_to_celsius(fahrenheit)
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print(f"The temperature in Celsius is {celsius:.2f}°C.")
        finally: # task 3
            print("Thank you for using the weather forecast application.")

if __name__ == "__main__":
    main()
