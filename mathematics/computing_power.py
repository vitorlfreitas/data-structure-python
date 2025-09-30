"""
In this file, we define a function to compute the power of a number recursively
"""


def power(base, exponent):
    """
    Computes the power of a number recursively.

    Parameters:
    base (float): The base number.
    exponent (int): The exponent (must be a non-negative integer).

    Returns:
    float: The result of base raised to the power of exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")

    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        return power(base, exponent // 2) * power(base, exponent // 2)

    return base * power(base, exponent // 2) * power(base, exponent // 2)


# Example usage:
print(power(2, 10))  # Output: 1024
print(power(3, 5))   # Output: 243
print(power(5, 0))   # Output: 1

# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack
