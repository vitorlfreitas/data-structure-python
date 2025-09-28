"""
In this file, we define a function to compute the factorial of a number using recursion.
"""

# Function to compute factorial of a number using recursion


def factorial_recursive(number: int) -> int:
    """
    Compute the factorial of a non-negative integer n using recursion
    """

    # Factorial is not defined for negative numbers
    if number < 0:
        return -1

    # Base case: Factorial of 0 is 1
    if number == 0:
        return 1

    # Recursive case: n! = n * (n-1)!
    return number * factorial_recursive(number - 1)


# Example usage
NUM1: int = 5
NUM2: int = 0

print(f"Factorial of {NUM1} is {factorial_recursive(NUM1)}")
print(f"Factorial of {NUM2} is {factorial_recursive(NUM2)}")

# Run this code in Python to see the output

# Time Complexity: O(n), where n is the input number.
# Space Complexity: O(n), as we are using the call stack for recursion.

# Note: Space complexity can be reduced to O(1) using iterative approach
# @See mathematics/factorial.py for iterative approach
