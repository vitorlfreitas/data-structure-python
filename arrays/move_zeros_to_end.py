"""
In this file we implement a method to move all zeros in an array to the end
"""


def move_zeros_to_end(arr: list) -> list:
    """
    Function to move all zeros in the array to the end
    """

    count = 0

    # Traverse the array
    for i, val in enumerate(arr):

        # If the element is not zero, swap it with the element at 'count' index
        if val != 0:
            # Swap elements
            arr[count], arr[i] = arr[i], arr[count]
            # Increment count of non-zero elements
            count += 1

    return arr


# Example usage:
myArray = [0, 1, 0, 3, 12]

print("Original array is:", myArray)

print("Array after moving zeros to end:", move_zeros_to_end(myArray))

# Time Complexity: O(n)
# Space Complexity: O(1)
