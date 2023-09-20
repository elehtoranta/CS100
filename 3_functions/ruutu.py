"""
COMP.CS.100: Tulostetaan ruutu
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Just printing squares.
"""

def print_box(width: int, height: int, mark: str):
    """Printing a box of given mark to the console.

    :param width: int, width of the box.
    :param height: int, height of the box.
    :param mark: str, the char used to mark the box.
    """
    for _ in range(height):
        print(mark * width)

def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
