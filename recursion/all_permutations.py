"""
In this module, we solve the problem of getting all the permutations of a given string
"""


def permute(s, i=0):
    """
    Method to print all permutations of a given string
    """

    # Convert string to list
    s = list(s)

    # Define a method to work recursively
    def helper(s, i):

        # Base Case
        if i == len(s) - 1:
            print("".join(s))
            return

        for j in range(i, len(s)):

            s[i], s[j] = s[j], s[i]

            helper(s, i + 1)

            s[i], s[j] = s[j], s[i]

    # Call the method
    helper(s, i)


# Example Usage
permute("ABCD")

# Time Complexity: O(n * n!)
# Space Complexity: O(n)
