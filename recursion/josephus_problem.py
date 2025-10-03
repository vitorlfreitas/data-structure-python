"""
In this module, we solve the Josephus Problem
"""


def josephus(n, k):
    """
    Solve the Josephus problem.
    n: number of people
    k: step count
    Returns the position of the last person standing (0-indexed).
    1. If there is only one person, they are the last person standing (base case).
    2. For n > 1, the position can be found recursively by reducing the problem size.
    The formula is: josephus(n, k) = (josephus(n-1, k) + k) % n
    This accounts for the circular nature of the problem.
    3. The result is adjusted to be 0-indexed.
    """

    # Base Case
    if n == 1:
        return 0

    return (josephus(n - 1, k) + k) % n


# Example Usage
print(josephus(4, 2)) # Output: 0
print(josephus(7, 3)) # Output: 3

# Time Complexity: O(n)
# Space Complexity: O(n) Due to recursion stack
