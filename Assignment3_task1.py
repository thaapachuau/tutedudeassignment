def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive step

# Sample number for calculating factorial
number = input("Enter a number: ")
sample_number = int(number)

# Call the factorial function
result = factorial(sample_number)

# Print the output
print(f"Factorial of {sample_number} is {result}")