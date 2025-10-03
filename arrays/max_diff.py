"""
In this file, we will find the maximum difference in an array 
"""


def get_max_diff(arr):
    """
    Finds the maximum difference within the array    
    :param arr: List[int] - The input array.
    :return: int - The maximum index difference.
    """

    max_value, min_value = arr[0], arr[0]
    max_diff = max_value - min_value

    i = 1
    while i < len(arr):

        if arr[i] > max_value:
            max_value = arr[i]

        if arr[i] < min_value:
            min_value = arr[i]

        max_diff = max(max_value - min_value, max_diff)

        i += 1

    return max_diff


# Example usage
array = [2, 3, 10, 6, 4, 8, 1]

max_diff_value = get_max_diff(array)

print(max_diff_value)  # Output: 9 (10 - 1)
# Time Complexity: O(n)
# Space Complexity: O(1)
