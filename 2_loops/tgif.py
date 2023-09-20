"""
COMP.CS.100: TGIF
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Counting Fridays of the year 2014.
"""


def main():
    FIRST_FRIDAY = 3  # Jan 3rd
    TICKER_ADJUST = 7 - FIRST_FRIDAY  # Tick every 7 days from 3rd

    ticker: int = TICKER_ADJUST  # 4; When days hit 3, ticker % 7 == 0
    day = month = 1
    while month <= 12:
        while day <= 31:
            if month in {4, 6, 9, 11} and day == 31:
                break
            if month == 2 and day == 29:
                break
            ticker += 1
            if ticker % 7 == 0:
                print(f'{day}.{month}.')
            day += 1
        day = 1
        month += 1

if __name__ == "__main__":
    main()
