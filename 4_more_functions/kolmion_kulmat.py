"""
COMP.CS.100: Kolmion kulmien laskeminen
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Calculating the angles of triangles using default values for right angles
"""

def calculate_angle(first: int, second: int = 90):
    """
    Calculate the angle of a third angle in a triangle. Angle.
    :param first: int, first angle.
    :param second: int, second angle.
    :return: int, third angle.
    """
    return 180 - first - second
