"""
In this file we implement a method to perform left rotation on an array
"""


def left_rotation(arr: list) -> list:
    """
    Function to perform left rotation on an array by d positions
    """
    n = len(arr)

    # Handle empty array case
    if n == 0:

        # If the array is empty, return it as is
        return arr

    temp = arr[0]

    for i in range(1, n):

        arr[i - 1] = arr[i]

    arr[n - 1] = temp

    return arr

# Example usage:


myArray = [1, 2, 3, 4, 5]

print("Original array is:", myArray)

print("Array after left rotation is:", left_rotation(myArray))

# Time Complexity for left_rotation is O(n)
# Space Complexity is O(1)
