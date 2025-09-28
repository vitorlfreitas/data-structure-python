""" 
    In this file, we define a function to compute the factorial of a number using loop.
    Later, we are going to explore to compute factorial using recursion.
"""
# Function to compute factorial of a number


def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer n
    """

    # Factorial is not defined for negative numbers
    if n < 0:
        return -1

    # Factorial of 0 is 1
    if n == 0:
        return 1

    res: int = 1

    # Compute factorial using a loop
    # This loop multiplies all integers from 1 to n
    for i in range(1, n + 1):
        # Multiply the current result by i
        res *= i
    # Return the computed factorial
    return res


# Example usage
NUM1: int = 5
NUM2: int = 0

print(f"Factorial of {NUM1} is {factorial(NUM1)}")
print(f"Factorial of {NUM2} is {factorial(NUM2)}")

# Run this code in Python to see the output

# Time Complexity: O(n), where n is the input number
# Space Complexity: O(1), as we are using a constant amount of space
