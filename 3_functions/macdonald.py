"""
COMP.CS.100: Old MacDonald Had a Farm
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***
Making virtual singing less painful with function calls.
"""

def print_verse(animal: str, sound: str):
    """Print the lyrics of the Old MacDonald with a function call.

    :param animal: str, name of the animal.
    :param sound: str, sound that the animal makes.
    """
    print(f'Old MACDONALD had a farm')
    print(f'E-I-E-I-O')
    print(f'And on his farm he had a {animal}')
    print(f'E-I-E-I-O')
    print(f'With a {sound} {sound} here')
    print(f'And a {sound} {sound} there')
    print(f'Here a {sound}, there a {sound}')
    print(f'Everywhere a {sound} {sound}')
    print(f'Old MacDonald had a farm')
    print(f'E-I-E-I-O')

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
