"""
COMP.CS.100: Käännä nimet oikein päin
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Reverse names from 'last, first' to 'first last'.
"""


def reverse_name(name: str):
    """
    Reverses the format of first and last name.
    :param name: Name in format "last, first"
    :return: Name reversed
    """
    name = name.split(',')
    for i in range(len(name)):
        name[i] = name[i].strip()
    name = ' '.join(reversed(name))
    return name.strip()
