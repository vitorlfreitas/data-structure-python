"""
In this file we implement a method to reverse an array
"""


def reverse_array(arr: list) -> list:
    """
    Function to reverse an array using two-pointer technique
    """
    left, right = 0, len(arr) - 1

    # Swap elements until the two pointers meet in the middle
    while left < right:
        # Swap the elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move towards the middle
        left += 1
        right -= 1

    return arr


# Example usage:
myArray = [1, 2, 3, 4, 5]

print("Original array is:", myArray)

print("Reversed array is:", reverse_array(myArray))

# Time Complexity for reverse_array is O(n)
# Space Complexity is O(1)
