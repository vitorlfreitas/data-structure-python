"""
bitwise_operations.py

Concise examples and explanations of Python bitwise operators.
Run as a script to see outputs.
"""

# Define two integers
# Under the hood, Python represents integers in binary format.
# For example, the integer 5 is represented as 101 in binary,
# and the integer 3 is represented as 011 in binary

A = 5  # Binary: 0101
B = 3  # Binary: 0011

# The AND operation between A and B
# It will check each bit of A and B.
# If both bits are 1, the result is 1; otherwise, it's 0

A_AND_B = A & B  # AND: 0001 

# Print the result of the AND operation
print(A, "&", B, "=", A_AND_B) # Should print 1 : 0001 in binary

# The OR operation between A and B
# It will check each bit of A and B.
# If at least one of the bits is 1, the result is 1; otherwise

A_OR_B = A | B  # OR: 0111

# Print the result of the OR operation
print(A, "|", B, "=", A_OR_B) # Should print 7 : 0111 in binary

# The XOR operation between A and B
# It will check each bit of A and B.
# If the bits are different, the result is 1; if they are the same, it's 0
A_XOR_B = A ^ B  # XOR: 0110

# Print the result of the XOR operation
print(A, "^", B, "=", A_XOR_B)

# The NOT operation on A
# It flips all the bits of A
A_NOT = ~A  # NOT: 1100

# Print the result of the NOT operation
print("~", A, "=", A_NOT)

# Note: The NOT operation inverts all bits and also changes the sign of the number.
# Example, ~5 results in -6 because of how negative numbers are represented

# The left shift operation on A by 1
# It shifts all bits in A to the left by 1 position
# And fills the rightmost bit with 0

C = 5 # Binary: 0101
C_LEFT_SHIFT = C << 1  # Left Shift: 1010

# Print the result of the left shift operation
print(C, "<< 1 =", C_LEFT_SHIFT) # Should print 10 : 1010 

# The right shift operation on A by 1
# It shifts all bits in A to the right by 1 position
# And fills the leftmost bit with 0 for positive numbers
C_RIGHT_SHIFT = C >> 1  # Right Shift: 0010

# Print the result of the right shift operation
print(C, ">> 1 =", C_RIGHT_SHIFT) # Should print 2 : 0010

# Important Fact about Bitwise Operations:

# The left and right shift operations should not be used in negative numbers
# The bitwise XOR is the most commonly used bitwise operation
# The left shift operation is equivalent to multiplying by 2
# The right shift operations are equivalent to dividing by 2

# Time Complexity:
# All bitwise operations run in constant time O(1)
# because they operate on a fixed number of bits (typically 32 or 64 bits).

# Space Complexity:
# All bitwise operations use a constant amount of space O(1)
