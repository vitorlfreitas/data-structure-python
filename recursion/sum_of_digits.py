"""
This module provides a recursive function to calculate the sum of digits in a given integer
"""


def sum_of_digits(n: int) -> int:
    """
    Function to calculate the sum of digits of a given integer using recursion.
    """

    # Handle negative numbers by converting to positive
    if n < 0:
        n = -n

    # Base case: if n is 0, the sum of digits is 0
    if n == 0:
        return 0

    last_digit = n % 10

    return last_digit + sum_of_digits(n // 10)


# Example usage:
print(sum_of_digits(12345))  # Output: 15
print(sum_of_digits(0))      # Output: 0
print(sum_of_digits(-678))   # Output: 21

# Time Complexity: O(d) where d is the number of digits in n
# Space Complexity: O(d) due to recursion stack
