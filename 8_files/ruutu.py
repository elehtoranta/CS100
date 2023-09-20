"""
COMP.CS.100: Ruutu syötetarkastuksin
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Printing boxes with error checks.
"""


def read_input(prompt: str) -> int:
    """Validates an input for a box.

    :param prompt: str, prompt for input().

    :return: int, a valid answer.
    """
    measure = 0
    while measure <= 0:
        try:
            measure = int(input(prompt))
        except:
            continue
    return measure

def print_box(width, height, mark):
    """Prints a box with given measures and character as a marker.

    :param width: int, width.
    :param height: int, height.
    :param mark: int, character signifying a box portion.
    """
    for _ in range(height):
        print(mark * width)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
