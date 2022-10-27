"""
COMP.CS.100: Virheilmoitukset
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
"""

def main():
    age: int = int(input("Please, enter your age: "))

    if age < 0:
        return

    if age < 7:
        ticket_price = 0.00
    elif age < 17:
        ticket_price = 1.02
    elif age < 25:
        ticket_price = 1.47
    else:
        ticket_price = 2.04

    print(f'Your ride will cost: {ticket_price}')


if __name__ == "__main__":
    main()