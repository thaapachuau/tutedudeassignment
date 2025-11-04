import math

def calculate_math_properties():
    """
    Asks the user for a number, then calculates and prints its square root,
    natural logarithm, and sine (in radians) using the math module.
    """
    try:
        num_str = input("Enter a number: ")
        number = float(num_str)

        # Calculate square root
        if number >= 0:
            square_root = math.sqrt(number)
            print(f"Square root : {square_root}")
        else:
            print(f"Cannot calculate the square root of a negative number ({number}).")

        # Calculate natural logarithm (log base e)
        if number > 0:
            natural_log = math.log(number)
            print(f"Logarithm : {natural_log}")
        else:
            print(f"Cannot calculate the natural logarithm of a non-positive number ({number}).")

        # Calculate sine (in radians)
        sine_value = math.sin(number)
        print(f"Sine: {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function to run the program
calculate_math_properties()