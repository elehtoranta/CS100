"""
COMP.CS.100: Montako löytyy?
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Reads a given amount of numbers, saves them to a list
and returns it.
"""


def input_to_list(n_args: int):
    """
    Saves n_args amount of given numbers to a list, returning it.
    :param n_args: int, amount of numbers queried.
    :return: list, containing numbers queried.
    """
    # Create an empty list for input
    numbers: list = []

    # Read and save given amount of numbers
    print(f'Enter {n_args} numbers:')
    for _ in range(n_args):
        numbers.append(int(input()))

    return numbers


def main():
    n_args: int = int(input('How many numbers do you want to process: '))
    numbers = input_to_list(n_args)

    queried = int(input('Enter the number to be searched: '))
    found: int = 0
    for number in numbers:
        if number == queried:
            found += 1

    if found > 0:
        print(f'{queried} shows up {found} times among '
              f'the numbers you have entered.')
    else:
        print(f'{queried} is not among the numbers you have entered.')


if __name__ == "__main__":
    main()
