"""
COMP.CS.100: Arvosanojen korvaus
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Reformatting grades from any passed value (1-5) to magic number 6.
"""


def convert_grades(grades: list):
    """
    Converts any grade from passed value (1-5) to a magic 'passed' signifier 6.
    :param grades: grade list
    :return: None
    """
    for i in range(len(grades)):
        if 0 < grades[i] <= 5:
            grades[i] = 6
