"""
COMP.CS.100: Inflaatiolaskin - projekti 1
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
Ohjelma selvittää suurimman kuukausittaisen inflaation nousun.
Deflaatiota ei huomioida.
"""


def main():
    # Create empty list for inflation rates
    rates: list = []

    # Fill the 'rates' list with inputs
    month: int = 1
    while True:
        input_str = input(f'Enter inflation rate for month {month}: ')
        if input_str == '':
            break
        current_rate = float(input_str)
        rates.append(current_rate)
        month += 1

    # Error check for 1) too few inputs
    if len(rates) < 2:
        print('Error: at least 2 monthly inflation rates must be entered.')
        return

    # Compare all elements in 'rates', keeping track of the maximum difference
    max_rate_diff: float = rates[1] - rates[0]
    for i in range(len(rates) - 1):  # - 1 to stop indexing within range.
        current_diff: float = rates[i + 1] - rates[i]
        if current_diff > max_rate_diff:
            max_rate_diff = current_diff

    # Print out the result
    print(f'Maximum inflation rate change was {max_rate_diff:.1f} points.')


if __name__ == "__main__":
    main()
