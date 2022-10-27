"""
COMP.CS.100: Lukusarjapeli (for)
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Descprition: Replacing numbers divisible with 3's and 7's with appropriate
words, for-loop edition.
"""


def main():
    max: int = int(input('How many numbers would you like to have? ')) + 1
    for n in range(1, max):
        if n % 3 == 0 and n % 7 == 0:
            print('zip boing')
        elif n % 3 == 0:
            print('zip')
        elif n % 7 == 0:
            print('boing')
        else:
            print(n)


if __name__ == "__main__":
    main()
