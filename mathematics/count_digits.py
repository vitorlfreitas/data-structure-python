# Count Digits in a Number passed as a parameter

# Function to count the number of digits in a given integer
def count_digits(number: int) -> int:

    # Handle negative numbers and zero
    if number < 0:
        # Make the number positive if it's negative
        number = -number  

    # Special case for zero
    if number == 0:
        # Zero has one digit
        return 1
    
    # Initialize digit count
    count = 0

    # Count digits by dividing the number by 10 until it becomes 0
    while number > 0:
        # In python, '//' is used for floor division
        # '/' would give a float result
        # Floor divide the number by 10 to remove the last digit
        number //= 10

        # Increment the digit count,
        # Similar to count = count + 1
        count += 1

    # Return the total count of digits
    return count

# Example usage
num1 = 938
num2 = -90
num3 = 0

print(f"The number of digits in {num1} is {count_digits(num1)}") 
print(f"The number of digits in {num2} is {count_digits(num2)}") 
print(f"The number of digits in {num3} is {count_digits(num3)}") 

# Run this code in a Python environment to see the output.

# Time Complexity: O(d), where d is the number of digits in the number.
# Space Complexity: O(1), as we are using a constant amount of space.