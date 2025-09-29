"""
Implements a function to compute the greatest common divisor (GCD)
Computes the GCD using the Euclidean Algorithm
"""


def gcd_optimized(a: int, b: int) -> int:
    """
    Compute the GCD of two integers a and b using the Euclidean Algorithm
    """
    if b == 0:
        return a

    return gcd_optimized(b, a % b)


# Usage example
NUM1: int = 56
NUM2: int = 98

print(
    f"GCD of {NUM1} and {NUM2} using optimized method is {gcd_optimized(NUM1, NUM2)}")

# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(log(min(a, b))) because of the recursion stack
