"""
In this file, we implement a method to find the second largest element in an array
"""


def find_second_largest(arr: list) -> int:
    """
    Function to find the second largest element in an array
    """

    # Handle edge cases
    if not arr or len(arr) < 2:
        return -1

    # Initialize first and second largest with the minimum possible value
    first = second = float('-inf')

    # Traverse the array to find the largest and second largest elements
    for num in arr:
        if num > first:
            second = first  # Update second largest
            first = num    # Update largest

        # Update second largest if current is between first and second
        elif first > num > second:
            second = num

    # Return -1 if no second largest found
    return second if second != float('-inf') else -1


# Example usage:
myArray = [3, 5, 2, 8, 1]

print("The second largest element is:", find_second_largest(myArray))

# Time Complexity for find_second_largest is O(n)
# Space Complexity is O(1)
