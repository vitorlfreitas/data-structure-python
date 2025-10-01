"""
This module provides a recursive function to check if a given string is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    """
    Function to check if a given string is a palindrome using recursion.
    """

    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) < 2:
        return True

    # Check the first and last characters for equality
    if s[0] != s[-1]:
        return False

    # Recursive case: check the substring without the first and last characters
    return is_palindrome(s[1:-1])


# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack
