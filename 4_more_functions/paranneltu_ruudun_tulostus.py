"""
COMP.CS.100: Paranneltu ruudun tulostus
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Printing a box with separate characters for the border and contents
"""


def print_box(width, height, border_mark='#', inner_mark=' '):
    """
    Printing a 2D box with given dimensions and char notation.
    :param width: int, width of box.
    :param height: int, height of box.
    :param border_mark: str, character denoting the box border.
    :param inner_mark: str, character denoting the box 'contents'.
    :return: None
    """
    # No print on either 0 dimension
    if 0 in [width, height]:
        return
    # Just one char of border_mark printed
    elif 1 in [width, height]:
        print(border_mark)
    # Print top and bottom rows full of border_mark,
    # rows in between border + content + border.
    else:
        for row in range(height):
            if row == 0 or row == height - 1:
                print(border_mark * width)
            else:
                print(border_mark + (inner_mark * (width - 2)) + border_mark)
    # Separating newline
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
