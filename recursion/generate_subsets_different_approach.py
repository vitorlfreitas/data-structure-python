"""
In this module, we provide a function to generate all subsets of a string using recursion.
"""


def generate_subsets(s, curr="", i=0):
    """
    Generate all subsets of the given string using recursion.
    """

    if i == len(s):
        return [curr]

    result = generate_subsets(s, curr, i + 1)
    result += generate_subsets(s, curr + s[i], i + 1)

    return list(set(result))


# Example usage:
print(generate_subsets("ab"))
# Output: ['', 'a', 'b', 'ab']

print(generate_subsets("abc"))
# Output: ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Note: The order of subsets in the output may vary since we are using a set to remove duplicates
