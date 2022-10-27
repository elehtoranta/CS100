"""
COMP.CS.100: Liukulukujen vertailu
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Comparing float values with an epsilon tolerance.
"""


def compare_floats(first, last, epsilon) -> bool:
    """ Compare two floats 'first' and 'last' to see if they equal. Due to
    float inaccuracy, an epsilon value is taken to specify tolerance.

    :param first: float, first float to be compared.
    :param last: float, second float to be compared.
    :param epsilon: constant to handle float inaccuracy.

    :return: bool, True if floats are equal within tolerance, False otherwise.
    """
    if abs(first - last) < epsilon:
        return True
    else:
        return False
