"""
In this file, we will find the largest element in an array.
"""


def left_rotate_by_d_times(arr, d):
    """
    This function rotates the array to the left by d times.
    :param arr: List[int] - The input array.
    :param d: int - The number of times to rotate the array.
    :return: List[int] - The rotated array.
    """

    # Size of the array
    n = len(arr)
    # Handle cases where d is greater than n
    d = d % n

    temp = [0] * d

    for i in range(d):
        temp[i] = arr[i]

    for j in range(d, n):
        arr[j - d] = arr[j]

    for k in range(0, d):
        arr[n - d + k] = temp[k]

    return arr


# Example usage
array = [1, 2, 3, 4, 5]

rotated_arr = left_rotate_by_d_times(array, 2)

print(rotated_arr)  # Output: [3, 4, 5, 1, 2]

# Time Complexity: O(n)
# Space Complexity: O(d) for the temporary array
