"""
Defines a recursive function to calculate the sum of the first n natural numbers
"""
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack


def sum_natural_numbers_tail_recursive(n, k = 0):
    """
    Computes the sum of the first n natural numbers using tail recursion"""

    # N should be a non-negative integer
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case for recursion
    if n == 0:
        return k

    return sum_natural_numbers_tail_recursive(n - 1, k + n)


# Example usage:
print(sum_natural_numbers_tail_recursive(5))  # Output: 15
print(sum_natural_numbers_tail_recursive(10))  # Output: 55
print(sum_natural_numbers_tail_recursive(0))  # Output: 0
