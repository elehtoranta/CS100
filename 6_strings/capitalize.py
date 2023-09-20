"""
COMP.CS.100: Isot alkukirjaimet paikoilleen
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Capitalizing a string
"""


def capitalize_initial_letters(s: str):
    """
    Format to capital first letter for all substrings in str[].
    :param s: str, string to format.
    :return: str, capitalized.
    """
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    s = ' '.join(s)
    return s

#
# def main():
#     print(capitalize_initial_letters(input("Yes: ")))
#
#
# if __name__ == "__main__":
#     main()
