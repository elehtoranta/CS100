"""
COMP.CS.100: Pricelist
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Searching prices for user's inputs.
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    """Getting prices for everyday products."""

    while True:
        name = input("Enter product name: ").strip()

        if not name or name.isspace():
            print('Bye!')
            return

        if name in PRICES:
            print(f'The price of {name} is {PRICES[name]:.2f} e')
        else:
            print(f'Error: {name} is unknown.')

if __name__ == "__main__":
    main()
