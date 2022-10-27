"""
COMP.CS.100: Listan indeksointi B
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Indexing a list backwards.
"""


def main():
    numbers: list = []
    print('Give 5 numbers:')
    for _ in range(5):
        numbers.append(int(input('Next number: ')))

    print('The numbers you entered, in reverse order:')
    for i in range(4, -1, -1):
        print(numbers[i])

if __name__ == "__main__":
    main()
