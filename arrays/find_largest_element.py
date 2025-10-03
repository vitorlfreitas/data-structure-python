"""
In this file, we will find the largest element in an array
"""


def find_largest_element(arr):
    """
    Function to find the largest element in an array
    """
    if not arr:
        return None  # Handle empty array case

    largest = arr[0]  # Assume the first element is the largest

    for num in arr:
        if num > largest:
            largest = num  # Update largest if current element is greater

    return largest


# Example usage:
myArray = [3, 5, 2, 8, 1]

print("The largest element is:", find_largest_element(myArray))

# Time Complexity for find_largest_element is O(n)
# Space Complexity is O(1)
