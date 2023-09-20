"""
COMP.CS.100: Tulostuksen muotoilu C
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Description: Adding correct formatting to a matrix of numbers.
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i*j:>4}', end='')
        print()

if __name__ == "__main__":
    main()
