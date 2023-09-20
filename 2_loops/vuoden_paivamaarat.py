"""
COMP.CS.100: Vuoden päivämäärät
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Prints the dates of a normal year.
"""


def main():

    day = month = 1
    while month <= 12:
        while day <= 31:
            if month in {4, 6, 9, 11} and day == 31:
                break
            if month == 2 and day == 29:
                break
            print(f"{day}.{month}.")
            day += 1
        month += 1
        day = 1


if __name__ == "__main__":
    main()
