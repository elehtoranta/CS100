"""
COMP.CS.100: Kivi-paperi-sakset
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
"""


def main():
    play_1: str = input('Player 1, enter your choice (R/P/S): ')
    play_2: str = input('Player 2, enter your choice (R/P/S): ')

    if play_1 == play_2:
        print("It's a tie!")
    elif (play_1 == 'S' and play_2 == 'P') \
            or (play_1 == 'P' and play_2 == 'R') \
            or (play_1 == 'R' and play_2 == 'S'):
        print('Player 1 won!')
    else:
        print('Player 2 won!')


if __name__ == "__main__":
    main()
