"""
In this file we implement a method to count the frequencies of all elements in a sorted array.
"""


def count_frequencies(arr):
    """
    Counts the frequencies of all elements in a sorted array
    """

    # Initialize frequency array
    frequency = []
    count = 1

    i = 1
    while i < len(arr):

        if arr[i] == arr[i - 1]:
            # Increment frequency count
            count += 1
        else:
            # Store the frequency of the previous element
            frequency.append(count)
            # Reset frequency count for the new element
            count = 1

        i += 1

    frequency.append(count)

    return frequency


# Example usage
array = [10, 10, 20, 20, 20, 30]

frequencies = count_frequencies(array)

print(frequencies)  # Output: [2, 3, 1]

# Time Complexity: O(n)
# Space Complexity: O(k) where k is the number of unique elements in the array
