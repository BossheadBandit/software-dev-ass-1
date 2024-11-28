import math

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
# Returns an error message if the second number is zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to raise the first number to the power of the second
def exponentiate(a, b):
    return a ** b

# Function to calculate the square root of a number
def sqrt(a):
    return math.sqrt(a)

# Function to calculate the base-10 logarithm of a number
def log_base_10(a):
    return math.log10(a)

# Function to calculate the natural logarithm of a number
def natural_log(a):
    return math.log(a)

# Function to calculate the sine of an angle (in degrees)
def sine(a):
    return math.sin(math.radians(a))

# Function to calculate the cosine of an angle (in degrees)
def cosine(a):
    return math.cos(math.radians(a))

# Function to calculate the tangent of an angle (in degrees)
def tangent(a):
    return math.tan(math.radians(a))

# Function to display the main menu of the calculator
def main_menu():
    print("Welcome to the Scientific Calculator please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm (base 10)")
    print("8. Natural Logarithm")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")

# Function to get a numeric input from the user
def get_input():
    try:
        return float(input("Enter a number: "))
    except ValueError:
        # If the input is not a number, prompt the user again
        print("Invalid input. Please enter a number.")
        return get_input()

# Main calculator function that runs in a loop
def calculator():
    while True:
        main_menu()  # Display the main menu
        choice = input("Select an operation (1-12): ")  # Get the user's choice
        
        if choice == '12':
            # Exit the loop if the user chooses to exit
            print("Exiting the calculator. Goodbye Thank you!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            # For operations that require two inputs
            a = get_input()  # Get the first number
            b = get_input()  # Get the second number
        else:
            # For operations that require one input
            a = get_input()  # Get the number
        
        # Perform the selected operation and print the result
        if choice == '1':
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            print(f"Result: {exponentiate(a, b)}")
        elif choice == '6':
            print(f"Result: {sqrt(a)}")
        elif choice == '7':
            print(f"Result: {log_base_10(a)}")
        elif choice == '8':
            print(f"Result: {natural_log(a)}")
        elif choice == '9':
            print(f"Result: {sine(a)}")
        elif choice == '10':
            print(f"Result: {cosine(a)}")
        elif choice == '11':
            print(f"Result: {tangent(a)}")
        else:
            # If the user enters an invalid choice
            print("Invalid choice. Please select a valid operation.")

# Entry point of the program
if __name__ == "__main__":
    calculator()