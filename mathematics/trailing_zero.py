"""
In this file, we define a function to count the zeros at the end of a factorial of a number
"""

# Function to count trailing zeros in factorial of a number

from factorial import factorial


def count_trailing_zeros(n: int) -> int:
    """
    Count the number of trailing zeros in n!
    """
    fact = factorial(n)
    count = 0

    # Count the number of trailing zeros
    while fact % 10 == 0:
        count += 1
        fact //= 10

    return count


# Example usage
NUM1: int = 5
NUM2: int = 10
NUM3: int = 100

print(f"Number of trailing zeros in {NUM1}! is {count_trailing_zeros(NUM1)}") # 1
print(f"Number of trailing zeros in {NUM2}! is {count_trailing_zeros(NUM2)}") # 2
print(f"Number of trailing zeros in {NUM3}! is {count_trailing_zeros(NUM3)}") # 24

# Run this code in Python to see the output

# Time Complexity: O(n) for computing factorial + O(d)
# Space Complexity: O(1), where d is the number of digits in n!
