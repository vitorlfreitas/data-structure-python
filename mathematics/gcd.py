"""
Implements a function to compute the greatest common divisor (GCD)
Computes the GCD of two integers using a Brute Force Approach
"""


def gcd_brute_force(a: int, b: int) -> int:
    """
    Compute the GCD of two integers a and b using a brute force approach
    """

    # Start from the minimum of a and b and go downwards
    gcd = min(a, b)

    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd = gcd - 1

    # GCD is 1 if no other common divisor is found
    return 1


# Usage example
NUM1: int = 56
NUM2: int = 98

print(
    f"GCD of {NUM1} and {NUM2} using brute force is {gcd_brute_force(NUM1, NUM2)}")

# Time Complexity: O(min(a, b))
# Space Complexity: O(1)
