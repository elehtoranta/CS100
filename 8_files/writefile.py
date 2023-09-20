"""
COMP.CS.100: Writing lines to a file
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*

Writing numbered lines to a file.
"""


def main():
    """Inputs a file with row numbering."""

    try:
        filename = input("Enter the name of the file: ")
        file = open(filename, 'w')
        print('Enter rows of text. Quit by entering an empty row.')

        i = 0
        while True:

            line = input()
            if not line:
                break

            i += 1
            print(f'{i} {line}', file=file)

        file.close()
        print(f'File {filename} has been written.')

    except:
        print(f'Writing the file {filename} was not successful.')


if __name__ == "__main__":
    main()
