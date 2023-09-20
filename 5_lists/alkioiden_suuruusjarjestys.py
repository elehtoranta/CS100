"""
COMP.CS.100: Listan alkioiden suuruusjärjestyksen tarkastelu
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Checking if a list is in ascending order.
"""

def is_the_list_in_order(ls: list):
    """
    Check if list ls is in ascending order.
    :param ls: list, list to be checked.
    :return: bool, True if the list ls is in ascending order, False otherwise.
    """
    # If there's 0 or 1 elements, the list is sorted by necessity
    if (len(ls)) <= 1:
        return True

    # Compare all elements for ascending sort
    for i in range(len(ls) - 1):
        if ls[i] > ls[i+1]:
            return False

    # If none of the looping comparisons evaluate False, return true.
    return True
