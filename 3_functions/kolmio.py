"""
COMP.CS.100: Kolmion pinta-ala
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Calculating the area of a triangle from it's side lengths.
"""

from math import sqrt

def area(first: float, second: float, third: float):
    """Returns the area of a triangle.

    :param first: float, first side.
    :param second: float, second side.
    :param third: float, third side.

    :return: float, area of the triangle.
    """
    s = (first + second + third) / 2.0
    return sqrt(s * (s - first) * (s - second) * (s - third))


def main():
    first = float(input("Enter the length of the first side: "))
    second = float(input("Enter the length of the second side: "))
    third = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(first, second, third):.1f}")

if __name__ == "__main__":
    main()
