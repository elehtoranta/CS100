"""
COMP.CS.100: Onko tylsää 2
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
A more elaborate check if the user is bored.
"""


def main():
    valid_input: bool = False
    while not valid_input:
        answer: str = input('Answer Y or N: ')
        if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
            valid_input = True
        else:
            print('Incorrect entry.')
    print(f'You answered {answer}')


if __name__ == "__main__":
    main()
