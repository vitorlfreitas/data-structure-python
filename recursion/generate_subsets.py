"""
In this module, we write a function to generate all subsets of a given set using recursion.
"""


def generate_subsets(string: str) -> list:
    """
    Generate all subsets of the given string using recursion.

    Args:
    string (str): The input string to generate subsets from.

    Returns:
    list: A list containing all subsets of the input string.
    """

    # Base Case: If the string is empty, return a list with an empty string
    if len(string) == 0:
        return [""]

    # Recursive Case: Get subsets of the string excluding the last character
    last_char = string[-1]
    subsets_excluding_last = generate_subsets(string[:-1])

    # Generate subsets including the last character
    subsets_including_last = [
        subset + last_char for subset in subsets_excluding_last]

    # Combine both subsets
    result = subsets_excluding_last + subsets_including_last

    # Remove duplicates if any
    return list(set(result))

# Example usage:

print(generate_subsets("ab"))
# Output: ['', 'a', 'b', 'ab'])

print(generate_subsets("abc"))
# Output: ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']