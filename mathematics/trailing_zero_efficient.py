"""
Function to calculate the number of trailing zeros in n! (n factorial)
Using an efficient approach based on counting factors of 5
"""


def count_trailing_zeros_efficient(n: int) -> int:
    """
    Count the number of trailing zeros in n! using an efficient method
    """
    count = 0

    i = 5
    while i <= n:
        count = count + (n // i)
        i *= 5

    return count


# Example usage
NUM1: int = 5
NUM2: int = 10
NUM3: int = 100

print(
    f"Number of trailing zeros in {NUM1}! is {count_trailing_zeros_efficient(NUM1)}")
print(
    f"Number of trailing zeros in {NUM2}! is {count_trailing_zeros_efficient(NUM2)}")
print(
    f"Number of trailing zeros in {NUM3}! is {count_trailing_zeros_efficient(NUM3)}")

# Run this code in Python to see the output

# Time Complexity: O(log_5(n)), where n is the input number
# Space Complexity: O(1)
