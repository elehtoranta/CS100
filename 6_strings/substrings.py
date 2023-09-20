"""
COMP.CS.100: Longest substring
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Finding the longest substring in a string.
"""

def get_ordered_substring_from_current_index(text: str) -> str:
    """
    Finds the longest substring from the current index of the calling
    function's string.

    :param text: str, string to be searched
    :return: str, the longest substring from current index
    """

    i = 0
    while i + 1 < len(text):
        if text[i+1] < text[i]:
            break
        i += 1

    # +1 to be end inclusive (python slices are end exclusive)
    return text[0:i+1]

def longest_substring_in_order(text: str) -> str:
    """
    Finds the longest substring of ascending lexicographical order in a
    given string.

    :param text: str, string to be searched
    :return: str, the longest substring found
    """

    current_longest_substring = ""

    for i in range(len(text)):

        # The function takes a slice from current index as its parameter.
        comparison_substring = get_ordered_substring_from_current_index(text[i:])

        if len(comparison_substring) > len(current_longest_substring):
            current_longest_substring = comparison_substring

            # if a substring is found, we can skip the rest of this
            # substring to avoid unnecessary checking.
            i += len(current_longest_substring)

    return current_longest_substring
