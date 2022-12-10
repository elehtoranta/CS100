"""
COMP.CS.100: Numbering lines in a file
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***

Numbering lines in a file.
"""


def main():
    """Outputs a file with row numbering."""

    with open(input("Enter the name of the file: "), 'r') as file:
        i = 0
        for line in file:
            i += 1
            print(f'{i} {line}', end='')


if __name__ == "__main__":
    main()
