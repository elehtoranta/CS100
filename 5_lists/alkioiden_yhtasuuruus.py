"""
COMP.CS.100: Listan alkioiden yhtäsuuruusvertailu
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Creating a function that tests and returns if all elements of a given list are
equal.
"""

def are_all_members_same(ls: list):
    """
    Checks if all the members of a given list ls are equal.
    :param ls: list, contains elements to test equality for.
    :return: bool, True if all elements are equal, False if inequal.
    """
    if len(ls) == 0:
        return True
    return min(ls) == max(ls)
