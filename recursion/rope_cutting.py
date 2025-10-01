"""
In this module, we solve the Rope Cutting Problem using recursion
Using brute-force recursion approach
"""


def cutting_rope(n, a, b, c):
    """
    Function to determine the maximum number of pieces a rope of length n can be cut into.
    Given that the pieces can only be of lengths a, b, or c.
    """

    # Base case: if n is exactly 0, no more cuts are needed
    if n == 0:
        return 0

    # If n becomes negative, no valid cuts can be made
    if n < 0:
        return -1

    # Recursively cut the rope by lengths a, b, and c
    res_a = cutting_rope(n - a, a, b, c)
    res_b = cutting_rope(n - b, a, b, c)
    res_c = cutting_rope(n - c, a, b, c)

    # Find the maximum of the three results
    res = max(res_a, res_b, res_c)

    # If all results are -1, return -1
    if res == -1:
        return -1

    # Otherwise, return the maximum result plus one for the current cut
    return res + 1


# Example usage:
rope_length = 5
cut_length_a = 2
cut_length_b = 5
cut_length_c = 1

print(cutting_rope(rope_length, cut_length_a,
      cut_length_b, cut_length_c))  # Output: 5

rope_length = 23
cut_length_a = 12
cut_length_b = 9
cut_length_c = 11

print(cutting_rope(rope_length, cut_length_a,
      cut_length_b, cut_length_c))  # Output: 2

rope_length = 5
cut_length_a = 4
cut_length_b = 2
cut_length_c = 6

print(cutting_rope(rope_length, cut_length_a,
      cut_length_b, cut_length_c))  # Output: -1

# Time Complexity: O(3^n)
# Space Complexity: O(n)
