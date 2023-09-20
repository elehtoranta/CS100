"""
COMP.CS.100: Akronyymin muodostaminen
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Create an acronym of input sentence and returns it.
"""


def create_an_acronym(name: str):
    """
    Creates an acronym of 'str'.
    :param name: str, Name to acronymize.
    :return: str, Acronym.
    """
    name = name.split()
    for i in range(len(name)):
        name[i] = name[i][0]
    return ''.join(name).upper()
