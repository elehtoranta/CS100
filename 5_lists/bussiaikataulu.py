"""
COMP.CS.100: Bussiaikataulu
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Searching for the next leaving bus at the specific stop.
"""


def main():
    timetable: list = [630, 1015, 1415, 1620, 1720, 2000]

    departure_time: int = int(input("Enter the time (as an integer): ") or 0)
    # Protecting an empty input.
    if departure_time == 0:
        return

    print('The next buses leave:')
    printed = i = 0
    for i in range(len(timetable)):
        if timetable[i] >= departure_time or departure_time > timetable[-1]:
            while printed < 3:
                print(timetable[i])
                printed += 1
                i = (i + 1) % len(timetable)


if __name__ == "__main__":
    main()
