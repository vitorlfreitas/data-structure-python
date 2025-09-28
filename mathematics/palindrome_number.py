# Palindrome Number Checker

# Function to check if a number is a palindrome

# A palindrome number reads the same backward as forward
# For example, 121 is a palindrome while 123 is not

def is_palindrome(number: int) -> bool:
    """
    Check if a given integer is a palindrome
    """

    # Store the original number to compare later
    original_number: int = number
    # Variable to hold the reversed number
    reversed_number: int = 0

    # Negative numbers are not palindromes
    if number < 0:
        return False

    # Reverse the number
    while number > 0:

        # Get the last digit of the number
        last_digit: int = number % 10
        # Build the reversed number
        reversed_number: int = reversed_number * 10 + last_digit
        # Remove the last digit from the number
        number //= 10

    return original_number == reversed_number


# Example usage
NUM1: int = 121
NUM2: int = -121
NUM3: int = 123
NUM4: int = 10
NUM5: int = 12321
print(f"Is {NUM1} a palindrome? {is_palindrome(NUM1)}")  # True
print(f"Is {NUM2} a palindrome? {is_palindrome(NUM2)}")  # False
print(f"Is {NUM3} a palindrome? {is_palindrome(NUM3)}")  # False
print(f"Is {NUM4} a palindrome? {is_palindrome(NUM4)}")  # False
print(f"Is {NUM5} a palindrome? {is_palindrome(NUM5)}")  # True

# Run this code in Python to see the output

# Time Complexity: O(d), where d is the number of digits in the number.
# Space Complexity: O(1), as we are using a constant amount of space.
