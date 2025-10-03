"""
In this file we implement a method to find all the leaders in an array.
A leader is an element which is greater than all the elements to its right side.
"""


def print_leaders(arr: list) -> list:

    current_leader = arr[-1]

    print(current_leader, end=" ")

    i = len(arr) - 2
    while i >= 0:

        if current_leader < arr[i]:

            current_leader = arr[i]
            print(current_leader, end=" ")

        i -= 1


# Example usage
array = [7, 10, 4, 10, 6, 5, 2]

print_leaders(array)  # Output: 2 5 6 10

# Time Complexity: O(n)
# Space Complexity: O(1)
