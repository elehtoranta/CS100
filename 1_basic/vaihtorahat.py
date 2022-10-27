"""
COMP.CS.100: Vaihtorahat
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
"""

def main():
    price: int = int(input('Purchase price: '))
    paid: int = int(input('Paid amount of money: '))
    change: int = paid - price
    tens = change // 10
    fives = (change - (tens * 10)) // 5
    twos = (change - (tens * 10) - (fives * 5)) // 2
    ones = (change - (tens * 10) - (fives * 5) - (twos * 2))

    if change <= 0:
        print('No change')
    else:
        print('Offer change:')
        if tens:
            print(f'{tens} ten-euro notes')
        if fives:
            print(f'{fives} five-euro notes')
        if twos:
            print(f'{twos} two-euro coins')
        if ones:
            print(f'{ones} one-euro coins')

if __name__ == "__main__":
    main()