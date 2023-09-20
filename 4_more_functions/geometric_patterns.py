"""
COMP.CS.100: Geometriset kuviot
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Printing circumference and area for a given geometric shape.
"""

from math import pi


def get_rect_circ(side1: float, side2: float) -> float:
    """
    Calculates a circumference of a rectangle.
    :param side1: float, first side of the rectangle.
    :param side2: float, second side of the rectangle.
    :return: float, circumference of the rectangle.
    """
    return (side1 * 2) + (side2 * 2)


def get_rect_area(side1: float, side2: float) -> float:
    """
    Calculates the area of a rectangle.
    :param side1: float, first side of the rectangle.
    :param side2: float, second side of the rectangle.
    :return: float, area of the rectangle.
    """
    return side1 * side2


def print_dimensions(area: float, circumference: float):
    """
    Outputs the area and circumference of a given shape.
    :param area: float, area of the shape.
    :param circumference: float, -- of the shape.
    :return: None
    """
    print(f'The circumference is {circumference:.2f}')
    print(f'The surface area is {area:.2f}')


def calc_square():
    """
    Calculates the area and circumference of a square.
    """
    while True:
        side: float = float(input("Enter the length of the square's side: "))
        if side > 0:
            break
    print_dimensions(get_rect_area(side, side), get_rect_circ(side, side))


def calc_rectangle():
    """
    Calculate the area and circumference of a rectangle.
    """
    while True:
        side1 = float(input("Enter the length of the rectangle's side 1: "))
        if side1 > 0:
            break
    while True:
        side2 = float(input("Enter the length of the rectangle's side 2: "))
        if side2 > 0:
            break
    print_dimensions(get_rect_area(side1, side2), get_rect_circ(side1, side2))


def calc_circle():
    """
    Queries for circle dimensions and prompts calculations and prints for
    results.
    """
    while True:
        radius = float(input("Enter the circle's radius: "))
        if radius > 0:
            break
    print_dimensions(pi * pow(radius, 2), 2 * pi * radius)


def menu():
    """
    Print a menu for user to select which geometric pattern to use in
    calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            calc_square()

        elif answer == "r":
            calc_rectangle()

        elif answer == "c":
            calc_circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
