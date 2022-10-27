"""
COMP.CS.100: Zip boing
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
=)
"""


def main():
    nums: int = int(input('How many numbers would you like to have? '))
    i: int = 1
    while i <= nums:
        if i % 3 == 0 or i % 7 == 0:
            if i % 3 == 0:
                print('zip', end='')
            if i % 7 == 0:
                if i % 3 == 0:
                    print(' ', end='')
                print('boing', end='')
            print()
        else:
            print(i)
        i += 1


if __name__ == "__main__":
    main()
