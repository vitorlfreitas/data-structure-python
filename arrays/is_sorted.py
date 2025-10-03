"""
In this file, we implement a method to check if an array is sorted
"""


def is_sorted(arr: list) -> bool:
    """
    Function to check if an array is sorted in non-decreasing order
    """
    if not arr:
        return True  # An empty array is considered sorted

    # Traverse the array
    for i in range(len(arr) - 1):

        # Compare current element with the next one
        if arr[i] > arr[i + 1]:

            # Found an element greater than the next one
            return False

    return True


# Example usage:
myArray = [1, 2, 2, 3, 4]

print("Is the array sorted?", is_sorted(myArray))

# Time Complexity for is_sorted is O(n)
# Space Complexity is O(1)
