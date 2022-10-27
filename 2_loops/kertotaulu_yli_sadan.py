"""
COMP.CS.100: Kertotaulu, kouluversio
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Prints the given multiplication table for the entered number.
"""


def main():
    num: int = int(input('Choose a number: '))

    i = 1
    while (i - 1) * num < 100:
        print(f'{i} * {num} = {i * num}')
        i += 1


if __name__ == "__main__":
    main()
