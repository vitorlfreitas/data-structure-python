"""
In this file, we solve some basic problems using bit manipulation techniques.
"""

# Problem 1: Check if a number is a power of two
# Time Complexity: O(1)
# Space Complexity: O(1)


def is_power_of_two(n):
    # If the number is less than or equal to 0, it cannot be a power of two
    if n <= 0:
        return False

    # A number is a power of two if it has exactly one bit set in its binary representation
    return (n & (n - 1)) == 0


# Test the function
print("Is 1 a power of two?", is_power_of_two(1))  # True
print("Is 8 a power of two?", is_power_of_two(8))  # True
print("Is 16 a power of two?", is_power_of_two(16))  # True

print("Is 18 a power of two?", is_power_of_two(18))  # False

# Problem 2: Find the most significant bit (MSB) position of a number
# Time Complexity: O(log n)
# Space Complexity: O(1)


def msb_position(n):
    if n <= 0:
        return -1  # Invalid input for MSB position

    position = 0
    while n > 1:
        n >>= 1  # Right shift the number by 1 to divide it by 2
        position += 1
    return position


# Test the function
print("MSB position of 1:", msb_position(1))  # 0
print("MSB position of 8:", msb_position(8))  # 3
print("MSB position of 16:", msb_position(16))  # 4
print("MSB position of 18:", msb_position(18))  # 4

# Problem 3: Find the XOR of all numbers from 1 to n
# Time Complexity:
# Space Complexity:


def xor_1_to_n(n):
    # Find the remainder of N by moduling it with 4
    remainder = n % 4
    # If remainder is 0, then XOR will be same as N
    if remainder == 0:
        return n

    # If remainder is 1, then XOR will be 1
    elif remainder == 1:
        return 1
    # If remainder is 2, then XOR will be N + 1
    elif remainder == 2:
        return n + 1
    # If remainder is 3, then XOR will be 0
    else:
        return 0


# Test the function
print("XOR of numbers from 1 to 7:", xor_1_to_n(7))  # 0
print("XOR of numbers from 1 to 6:", xor_1_to_n(6))  # 7
