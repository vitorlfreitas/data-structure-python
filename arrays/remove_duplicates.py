"""
In this file we implement a method to remove duplicates from a sorted array
"""


def remove_duplicates(arr: list) -> list:
    """
    Function to remove duplicates from an array while maintaining the order of first occurrences
    """
    # Handle empty array case
    if not arr:
        return []

    result = 1

    # Traverse the array starting from the second element
    for i in range(1, len(arr)):

        # Compare with the previous element
        if arr[i] != arr[i - 1]:

            arr[result] = arr[i]
            result += 1

    return arr[:result]


# Example usage:
myArray = [1, 2, 2, 3, 4, 4, 5]

print("Original array is:", myArray)

print("Array after removing duplicates:", remove_duplicates(myArray))

# Time Complexity: O(n)
# Space Complexity: O(1)
