
"""
COMP.CS.100: Laske abbat
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Kuvaus: Counts a the number of times a legendary Swedish band appears
in a given string.
"""

def count_abbas(string: str) -> int:
    """
    Counts a the number of times a legendary Swedish band appears
    in a given string.

    :param string: str, string to be searched for abba.
    :return: int, number of occurances of abba.
    """

    string_len = len(string)
    abbas: int = 0

    for i in range(string_len):
        if i + 3 >= string_len:
            break
        elif string[i:i+4] == "abba":
            abbas += 1

    return abbas
